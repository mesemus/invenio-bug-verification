## Collected Warnings

### Patched

#### Warning 1 - 30 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-github` | 6 |
| `invenio-records-ui` | 5 |
| `invenio-userprofiles` | 5 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |

#### Warning 2 - 8 occurrences

DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 8 |

#### Warning 3 - 8 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-notifications` | 2 |
| `invenio-records-ui` | 2 |

#### Warning 4 - 6 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-notifications` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-userprofiles` | 1 |

#### Warning 5 - 6 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-notifications` | 2 |

#### Warning 6 - 5 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-cache` | 1 |
| `invenio-github` | 1 |

#### Warning 7 - 5 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 3 |
| `invenio-banners` | 2 |

#### Warning 8 - 4 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-userprofiles` | 1 |

#### Warning 9 - 4 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |
| `invenio-records-ui` | 1 |

#### Warning 10 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 11 - 4 occurrences

SyntaxWarning: invalid escape sequence '\_'

| Package | Count |
|---------|-------|
| `invenio-mail` | 4 |

#### Warning 12 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |

#### Warning 13 - 3 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |

#### Warning 14 - 3 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |

#### Warning 15 - 3 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |

#### Warning 16 - 3 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-github` | 1 |

#### Warning 17 - 3 occurrences

SyntaxWarning: invalid escape sequence '\*'

| Package | Count |
|---------|-------|
| `invenio-mail` | 3 |

#### Warning 18 - 3 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-notifications` | 1 |

#### Warning 19 - 2 occurrences

DeprecationWarning: 'pkgutil.get_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 2 |

#### Warning 20 - 2 occurrences

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-db` | 1 |

#### Warning 21 - 2 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |

#### Warning 22 - 1 occurrence

DeprecationWarning: 'pkgutil.find_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 23 - 1 occurrence

DeprecationWarning: Attribute s is deprecated and will be removed in Python 3.14; use value instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 24 - 1 occurrence

DeprecationWarning: Please use hash_password instead of encrypt_password.

| Package | Count |
|---------|-------|
| `invenio-records-ui` | 1 |

#### Warning 25 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 26 - 1 occurrence

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 27 - 1 occurrence

DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 28 - 1 occurrence

DeprecationWarning: current_userprofile is deprecated, use current_user instead

| Package | Count |
|---------|-------|
| `invenio-userprofiles` | 1 |

#### Warning 29 - 1 occurrence

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |

#### Warning 30 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 31 - 1 occurrence

PendingDeprecationWarning: This feature is deprecated.

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 32 - 1 occurrence

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-records-ui` | 1 |

#### Warning 33 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 34 - 1 occurrence

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-records-ui` | 1 |

#### Warning 35 - 1 occurrence

SyntaxWarning: "is" with 'str' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 36 - 1 occurrence

SyntaxWarning: invalid escape sequence '\ '

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 37 - 1 occurrence

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 38 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 39 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 40 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |


