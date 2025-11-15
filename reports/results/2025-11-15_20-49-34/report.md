# Invenio Bugfix Verification Results

_Last updated: 2025-11-15 20:49:34 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 52 |
| **Patched Packages** | 52 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 12 |
| ⚠️  Still Failing | 18 |
| ℹ️  No Change | 22 |

## 🔧 Configured Patches

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-db` <br/>  [patched](packages/invenio-db/test-output-patched.txt)  [warnings-patched](packages/invenio-db/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-access` <br/>  [patched](packages/invenio-access/test-output-patched.txt)  [warnings-patched](packages/invenio-access/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-accounts` <br/>  [original](packages/invenio-accounts/test-output-original.txt)  [patched](packages/invenio-accounts/test-output-patched.txt)  [warnings-original](packages/invenio-accounts/warnings-original.md)  [warnings-patched](packages/invenio-accounts/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-administration` <br/>  [patched](packages/invenio-administration/test-output-patched.txt)  [warnings-patched](packages/invenio-administration/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-app-rdm` <br/>  [patched](packages/invenio-app-rdm/test-output-patched.txt)  [warnings-patched](packages/invenio-app-rdm/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-app` <br/>  [original](packages/invenio-app/test-output-original.txt)  [patched](packages/invenio-app/test-output-patched.txt)  [warnings-original](packages/invenio-app/warnings-original.md)  [warnings-patched](packages/invenio-app/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-assets` <br/>  [original](packages/invenio-assets/test-output-original.txt)  [patched](packages/invenio-assets/test-output-patched.txt)  [warnings-original](packages/invenio-assets/warnings-original.md)  [warnings-patched](packages/invenio-assets/warnings-patched.md) | pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-audit-logs` <br/>  [patched](packages/invenio-audit-logs/test-output-patched.txt)  [warnings-patched](packages/invenio-audit-logs/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-banners` <br/>  [original](packages/invenio-banners/test-output-original.txt)  [patched](packages/invenio-banners/test-output-patched.txt)  [warnings-original](packages/invenio-banners/warnings-original.md)  [warnings-patched](packages/invenio-banners/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-base` <br/>  [patched](packages/invenio-base/test-output-patched.txt)  [warnings-patched](packages/invenio-base/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-cache` <br/>  [patched](packages/invenio-cache/test-output-patched.txt)  [warnings-patched](packages/invenio-cache/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-celery` <br/>  [original](packages/invenio-celery/test-output-original.txt)  [patched](packages/invenio-celery/test-output-patched.txt)  [warnings-original](packages/invenio-celery/warnings-original.md)  [warnings-patched](packages/invenio-celery/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-checks` <br/>  [original](packages/invenio-checks/test-output-original.txt)  [patched](packages/invenio-checks/test-output-patched.txt)  [warnings-original](packages/invenio-checks/warnings-original.md)  [warnings-patched](packages/invenio-checks/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-collections` <br/>  [original](packages/invenio-collections/test-output-original.txt)  [patched](packages/invenio-collections/test-output-patched.txt)  [warnings-original](packages/invenio-collections/warnings-original.md)  [warnings-patched](packages/invenio-collections/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-communities` <br/>  [patched](packages/invenio-communities/test-output-patched.txt)  [warnings-patched](packages/invenio-communities/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-config` <br/>  [original](packages/invenio-config/test-output-original.txt)  [patched](packages/invenio-config/test-output-patched.txt)  [warnings-original](packages/invenio-config/warnings-original.md)  [warnings-patched](packages/invenio-config/warnings-patched.md) | pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-db` <br/>  [patched](packages/invenio-db/test-output-patched.txt)  [warnings-patched](packages/invenio-db/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` <br/>  [patched](packages/invenio-drafts-resources/test-output-patched.txt)  [warnings-patched](packages/invenio-drafts-resources/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-files-rest` <br/>  [patched](packages/invenio-files-rest/test-output-patched.txt)  [warnings-patched](packages/invenio-files-rest/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` <br/>  [original](packages/invenio-formatter/test-output-original.txt)  [patched](packages/invenio-formatter/test-output-patched.txt)  [warnings-original](packages/invenio-formatter/warnings-original.md)  [warnings-patched](packages/invenio-formatter/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-github` <br/>  [patched](packages/invenio-github/test-output-patched.txt)  [warnings-patched](packages/invenio-github/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-i18n` <br/>  [patched](packages/invenio-i18n/test-output-patched.txt)  [warnings-patched](packages/invenio-i18n/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` <br/>  [patched](packages/invenio-indexer/test-output-patched.txt)  [warnings-patched](packages/invenio-indexer/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` <br/>  [original](packages/invenio-jobs/test-output-original.txt)  [patched](packages/invenio-jobs/test-output-patched.txt)  [warnings-original](packages/invenio-jobs/warnings-original.md)  [warnings-patched](packages/invenio-jobs/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-jsonschemas` <br/>  [original](packages/invenio-jsonschemas/test-output-original.txt)  [patched](packages/invenio-jsonschemas/test-output-patched.txt)  [warnings-original](packages/invenio-jsonschemas/warnings-original.md)  [warnings-patched](packages/invenio-jsonschemas/warnings-patched.md) | pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-logging` <br/>  [original](packages/invenio-logging/test-output-original.txt)  [patched](packages/invenio-logging/test-output-patched.txt)  [warnings-original](packages/invenio-logging/warnings-original.md)  [warnings-patched](packages/invenio-logging/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-mail` <br/>  [patched](packages/invenio-mail/test-output-patched.txt)  [warnings-patched](packages/invenio-mail/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` <br/>  [patched](packages/invenio-notifications/test-output-patched.txt)  [warnings-patched](packages/invenio-notifications/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` <br/>  [original](packages/invenio-oaiserver/test-output-original.txt)  [patched](packages/invenio-oaiserver/test-output-patched.txt)  [warnings-original](packages/invenio-oaiserver/warnings-original.md)  [warnings-patched](packages/invenio-oaiserver/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-oauth2server` <br/>  [original](packages/invenio-oauth2server/test-output-original.txt)  [patched](packages/invenio-oauth2server/test-output-patched.txt)  [warnings-original](packages/invenio-oauth2server/warnings-original.md)  [warnings-patched](packages/invenio-oauth2server/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-oauthclient` <br/>  [original](packages/invenio-oauthclient/test-output-original.txt)  [patched](packages/invenio-oauthclient/test-output-patched.txt)  [warnings-original](packages/invenio-oauthclient/warnings-original.md)  [warnings-patched](packages/invenio-oauthclient/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-pages` <br/>  [patched](packages/invenio-pages/test-output-patched.txt)  [warnings-patched](packages/invenio-pages/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` <br/>  [original](packages/invenio-pidstore/test-output-original.txt)  [patched](packages/invenio-pidstore/test-output-patched.txt)  [warnings-original](packages/invenio-pidstore/warnings-original.md)  [warnings-patched](packages/invenio-pidstore/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-previewer` <br/>  [original](packages/invenio-previewer/test-output-original.txt)  [patched](packages/invenio-previewer/test-output-patched.txt)  [warnings-original](packages/invenio-previewer/warnings-original.md)  [warnings-patched](packages/invenio-previewer/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-queues` <br/>  [patched](packages/invenio-queues/test-output-patched.txt)  [warnings-patched](packages/invenio-queues/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-rdm-records` <br/>  [original](packages/invenio-rdm-records/test-output-original.txt)  [patched](packages/invenio-rdm-records/test-output-patched.txt)  [warnings-original](packages/invenio-rdm-records/warnings-original.md)  [warnings-patched](packages/invenio-rdm-records/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-files` <br/>  [original](packages/invenio-records-files/test-output-original.txt)  [patched](packages/invenio-records-files/test-output-patched.txt)  [warnings-original](packages/invenio-records-files/warnings-original.md)  [warnings-patched](packages/invenio-records-files/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-records-permissions` <br/>  [original](packages/invenio-records-permissions/test-output-original.txt)  [patched](packages/invenio-records-permissions/test-output-patched.txt)  [warnings-original](packages/invenio-records-permissions/warnings-original.md)  [warnings-patched](packages/invenio-records-permissions/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-records-resources` <br/>  [original](packages/invenio-records-resources/test-output-original.txt)  [patched](packages/invenio-records-resources/test-output-patched.txt)  [warnings-original](packages/invenio-records-resources/warnings-original.md)  [warnings-patched](packages/invenio-records-resources/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-rest` <br/>  [original](packages/invenio-records-rest/test-output-original.txt)  [patched](packages/invenio-records-rest/test-output-patched.txt)  [warnings-original](packages/invenio-records-rest/warnings-original.md)  [warnings-patched](packages/invenio-records-rest/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-ui` <br/>  [original](packages/invenio-records-ui/test-output-original.txt)  [patched](packages/invenio-records-ui/test-output-patched.txt)  [warnings-original](packages/invenio-records-ui/warnings-original.md)  [warnings-patched](packages/invenio-records-ui/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-records` <br/>  [patched](packages/invenio-records/test-output-patched.txt)  [warnings-patched](packages/invenio-records/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-requests` <br/>  [patched](packages/invenio-requests/test-output-patched.txt)  [warnings-patched](packages/invenio-requests/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-rest` <br/>  [original](packages/invenio-rest/test-output-original.txt)  [patched](packages/invenio-rest/test-output-patched.txt)  [warnings-original](packages/invenio-rest/warnings-original.md)  [warnings-patched](packages/invenio-rest/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-search-ui` <br/>  [original](packages/invenio-search-ui/test-output-original.txt)  [patched](packages/invenio-search-ui/test-output-patched.txt)  [warnings-original](packages/invenio-search-ui/warnings-original.md)  [warnings-patched](packages/invenio-search-ui/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-search` <br/>  [original](packages/invenio-search/test-output-original.txt)  [patched](packages/invenio-search/test-output-patched.txt)  [warnings-original](packages/invenio-search/warnings-original.md)  [warnings-patched](packages/invenio-search/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-sitemap` <br/>  [patched](packages/invenio-sitemap/test-output-patched.txt)  [warnings-patched](packages/invenio-sitemap/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-stats` <br/>  [original](packages/invenio-stats/test-output-original.txt)  [patched](packages/invenio-stats/test-output-patched.txt)  [warnings-original](packages/invenio-stats/warnings-original.md)  [warnings-patched](packages/invenio-stats/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-theme` <br/>  [patched](packages/invenio-theme/test-output-patched.txt)  [warnings-patched](packages/invenio-theme/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-userprofiles` <br/>  [patched](packages/invenio-userprofiles/test-output-patched.txt)  [warnings-patched](packages/invenio-userprofiles/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-users-resources` <br/>  [original](packages/invenio-users-resources/test-output-original.txt)  [patched](packages/invenio-users-resources/test-output-patched.txt)  [warnings-original](packages/invenio-users-resources/warnings-original.md)  [warnings-patched](packages/invenio-users-resources/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-vocabularies` <br/>  [original](packages/invenio-vocabularies/test-output-original.txt)  [patched](packages/invenio-vocabularies/test-output-patched.txt)  [warnings-original](packages/invenio-vocabularies/warnings-original.md)  [warnings-patched](packages/invenio-vocabularies/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-webhooks` <br/>  [original](packages/invenio-webhooks/test-output-original.txt)  [patched](packages/invenio-webhooks/test-output-patched.txt)  [warnings-original](packages/invenio-webhooks/warnings-original.md)  [warnings-patched](packages/invenio-webhooks/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |

## Collected Warnings

### Original

#### Warning 1 - 30 occurrences

blah

| Package | Count |
|---------|-------|
| `invenio-accounts` | 1 |
| `invenio-app` | 1 |
| `invenio-assets` | 1 |
| `invenio-banners` | 1 |
| `invenio-celery` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-config` | 1 |
| `invenio-formatter` | 1 |
| `invenio-jobs` | 1 |
| `invenio-jsonschemas` | 1 |
| `invenio-logging` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-previewer` | 1 |
| `invenio-rdm-records` | 1 |
| `invenio-records-files` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-rest` | 1 |
| `invenio-search` | 1 |
| `invenio-search-ui` | 1 |
| `invenio-stats` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |
| `invenio-webhooks` | 1 |


### Patched

#### Warning 1 - 52 occurrences

blah

| Package | Count |
|---------|-------|
| `invenio-access` | 1 |
| `invenio-accounts` | 1 |
| `invenio-administration` | 1 |
| `invenio-app` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-assets` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-base` | 1 |
| `invenio-cache` | 1 |
| `invenio-celery` | 1 |
| `invenio-checks` | 1 |
| `invenio-collections` | 1 |
| `invenio-communities` | 1 |
| `invenio-config` | 1 |
| `invenio-db` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-files-rest` | 1 |
| `invenio-formatter` | 1 |
| `invenio-github` | 1 |
| `invenio-i18n` | 1 |
| `invenio-indexer` | 1 |
| `invenio-jobs` | 1 |
| `invenio-jsonschemas` | 1 |
| `invenio-logging` | 1 |
| `invenio-mail` | 1 |
| `invenio-notifications` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-oauth2server` | 1 |
| `invenio-oauthclient` | 1 |
| `invenio-pages` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-previewer` | 1 |
| `invenio-queues` | 1 |
| `invenio-rdm-records` | 1 |
| `invenio-records` | 1 |
| `invenio-records-files` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-records-rest` | 1 |
| `invenio-records-ui` | 1 |
| `invenio-requests` | 1 |
| `invenio-rest` | 1 |
| `invenio-search` | 1 |
| `invenio-search-ui` | 1 |
| `invenio-sitemap` | 1 |
| `invenio-stats` | 1 |
| `invenio-theme` | 1 |
| `invenio-userprofiles` | 1 |
| `invenio-users-resources` | 1 |
| `invenio-vocabularies` | 1 |
| `invenio-webhooks` | 1 |


---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._
