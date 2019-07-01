# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Functions for module management."""

# Do not add any imports to non-standard modules here.
import os
import site
import sys
import warnings

KNOWN_WARNING_SIGNATURES = [
    # Known conflicts between datastore and datastore_v1 protos.
    r'Conflict register for file.*is already defined in file',
]


def disable_known_module_warnings():
  """Disable known and harmless module warnings."""
  for message_regex in KNOWN_WARNING_SIGNATURES:
    warnings.filterwarnings('ignore', message_regex)


def _patch_appengine_modules_for_bots():
  """Patch out App Engine reliant behaviour from bots."""
  if os.getenv('SERVER_SOFTWARE'):
    # Not applicable on App Engine.
    return

  # google.auth uses App Engine credentials based on importability of
  # google.appengine.api.app_identity.
  try:
    from google.auth import app_engine as auth_app_engine
    if auth_app_engine.app_identity:
      auth_app_engine.app_identity = None
  except ImportError:
    pass


def _config_modules_directory(root_directory):
  """Get the config modules directory."""
  config_dir = os.getenv('CONFIG_DIR_OVERRIDE')
  if not config_dir:
    config_dir = os.path.join(root_directory, 'src', 'appengine', 'config')

  return os.path.join(config_dir, 'modules')


def fix_module_search_paths():
  """Add directories that we must be able to import from to path."""
  root_directory = os.environ['ROOT_DIR']
  source_directory = os.path.join(root_directory, 'src')

  python_path = os.getenv('PYTHONPATH', '').split(os.pathsep)

  third_party_libraries_directory = os.path.join(source_directory,
                                                 'third_party')
  config_modules_directory = _config_modules_directory(root_directory)

  if (os.path.exists(config_modules_directory) and
      config_modules_directory not in sys.path):
    sys.path.insert(0, config_modules_directory)
    python_path.insert(0, config_modules_directory)

  if third_party_libraries_directory not in sys.path:
    sys.path.insert(0, third_party_libraries_directory)
    python_path.insert(0, third_party_libraries_directory)

  python_source_directory = os.path.join(source_directory, 'python')
  if python_source_directory not in sys.path:
    sys.path.insert(0, python_source_directory)
    python_path.insert(0, python_source_directory)

  if source_directory not in sys.path:
    sys.path.insert(0, source_directory)
    python_path.insert(0, source_directory)

  # Error logging must be deferred until the end of the function since these
  # fixes are needed to import the logs module.
  errors = []

  # Work around google package issues with App Engine SDK.
  try:
    import dev_appserver
    dev_appserver.fix_google_path()
  except (ImportError, RuntimeError) as error:
    errors.append('Fixing google import failed: %s' % error)

  # Make protobuf compatible with appengine.
  # FIXME(unassigned): remove try-except once we confirm it works.
  try:
    import google
    protobuf_directory = os.path.join(third_party_libraries_directory, 'google')
    google.__path__.append(protobuf_directory)

  except (ImportError, RuntimeError) as error:
    errors.append('Fixing protobuf-appengine compatibility failed: %s' % error)

  os.environ['PYTHONPATH'] = os.pathsep.join(python_path)

  # Add site directory to make from imports work in google namespace.
  site.addsitedir(third_party_libraries_directory)

  disable_known_module_warnings()
  _patch_appengine_modules_for_bots()

  # Since paths have now been fixed, import the custom logs module.
  from metrics import logs
  for error in errors:
    logs.log_error(error)
