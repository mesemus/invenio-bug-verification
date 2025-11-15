# Invenio Bugfix Verification Results

_Last updated: 2025-11-15 21:18:15 UTC_

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
| ❌ Regressions | 10 |
| ⚠️  Still Failing | 14 |
| ℹ️  No Change | 28 |

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
| `invenio-accounts` <br/>  [patched](packages/invenio-accounts/test-output-patched.txt)  [warnings-patched](packages/invenio-accounts/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-administration` <br/>  [original](packages/invenio-administration/test-output-original.txt)  [patched](packages/invenio-administration/test-output-patched.txt)  [warnings-original](packages/invenio-administration/warnings-original.md)  [warnings-patched](packages/invenio-administration/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-app-rdm` <br/>  [original](packages/invenio-app-rdm/test-output-original.txt)  [patched](packages/invenio-app-rdm/test-output-patched.txt)  [warnings-original](packages/invenio-app-rdm/warnings-original.md)  [warnings-patched](packages/invenio-app-rdm/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-app` <br/>  [original](packages/invenio-app/test-output-original.txt)  [patched](packages/invenio-app/test-output-patched.txt)  [warnings-original](packages/invenio-app/warnings-original.md)  [warnings-patched](packages/invenio-app/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-assets` <br/>  [patched](packages/invenio-assets/test-output-patched.txt)  [warnings-patched](packages/invenio-assets/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` <br/>  [original](packages/invenio-audit-logs/test-output-original.txt)  [patched](packages/invenio-audit-logs/test-output-patched.txt)  [warnings-original](packages/invenio-audit-logs/warnings-original.md)  [warnings-patched](packages/invenio-audit-logs/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-banners` <br/>  [patched](packages/invenio-banners/test-output-patched.txt)  [warnings-patched](packages/invenio-banners/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-base` <br/>  [original](packages/invenio-base/test-output-original.txt)  [patched](packages/invenio-base/test-output-patched.txt)  [warnings-original](packages/invenio-base/warnings-original.md)  [warnings-patched](packages/invenio-base/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-cache` <br/>  [patched](packages/invenio-cache/test-output-patched.txt)  [warnings-patched](packages/invenio-cache/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-celery` <br/>  [patched](packages/invenio-celery/test-output-patched.txt)  [warnings-patched](packages/invenio-celery/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-checks` <br/>  [patched](packages/invenio-checks/test-output-patched.txt)  [warnings-patched](packages/invenio-checks/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-collections` <br/>  [patched](packages/invenio-collections/test-output-patched.txt)  [warnings-patched](packages/invenio-collections/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-communities` <br/>  [original](packages/invenio-communities/test-output-original.txt)  [patched](packages/invenio-communities/test-output-patched.txt)  [warnings-original](packages/invenio-communities/warnings-original.md)  [warnings-patched](packages/invenio-communities/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-config` <br/>  [original](packages/invenio-config/test-output-original.txt)  [patched](packages/invenio-config/test-output-patched.txt)  [warnings-original](packages/invenio-config/warnings-original.md)  [warnings-patched](packages/invenio-config/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-db` <br/>  [patched](packages/invenio-db/test-output-patched.txt)  [warnings-patched](packages/invenio-db/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` <br/>  [original](packages/invenio-drafts-resources/test-output-original.txt)  [patched](packages/invenio-drafts-resources/test-output-patched.txt)  [warnings-original](packages/invenio-drafts-resources/warnings-original.md)  [warnings-patched](packages/invenio-drafts-resources/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-files-rest` <br/>  [patched](packages/invenio-files-rest/test-output-patched.txt)  [warnings-patched](packages/invenio-files-rest/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` <br/>  [patched](packages/invenio-formatter/test-output-patched.txt)  [warnings-patched](packages/invenio-formatter/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-github` <br/>  [patched](packages/invenio-github/test-output-patched.txt)  [warnings-patched](packages/invenio-github/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-i18n` <br/>  [patched](packages/invenio-i18n/test-output-patched.txt)  [warnings-patched](packages/invenio-i18n/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` <br/>  [original](packages/invenio-indexer/test-output-original.txt)  [patched](packages/invenio-indexer/test-output-patched.txt)  [warnings-original](packages/invenio-indexer/warnings-original.md)  [warnings-patched](packages/invenio-indexer/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-jobs` <br/>  [patched](packages/invenio-jobs/test-output-patched.txt)  [warnings-patched](packages/invenio-jobs/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jsonschemas` <br/>  [original](packages/invenio-jsonschemas/test-output-original.txt)  [patched](packages/invenio-jsonschemas/test-output-patched.txt)  [warnings-original](packages/invenio-jsonschemas/warnings-original.md)  [warnings-patched](packages/invenio-jsonschemas/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-logging` <br/>  [patched](packages/invenio-logging/test-output-patched.txt)  [warnings-patched](packages/invenio-logging/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-mail` <br/>  [patched](packages/invenio-mail/test-output-patched.txt)  [warnings-patched](packages/invenio-mail/warnings-patched.md) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` <br/>  [patched](packages/invenio-notifications/test-output-patched.txt)  [warnings-patched](packages/invenio-notifications/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` <br/>  [original](packages/invenio-oaiserver/test-output-original.txt)  [patched](packages/invenio-oaiserver/test-output-patched.txt)  [warnings-original](packages/invenio-oaiserver/warnings-original.md)  [warnings-patched](packages/invenio-oaiserver/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-oauth2server` <br/>  [patched](packages/invenio-oauth2server/test-output-patched.txt)  [warnings-patched](packages/invenio-oauth2server/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oauthclient` <br/>  [patched](packages/invenio-oauthclient/test-output-patched.txt)  [warnings-patched](packages/invenio-oauthclient/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-pages` <br/>  [original](packages/invenio-pages/test-output-original.txt)  [patched](packages/invenio-pages/test-output-patched.txt)  [warnings-original](packages/invenio-pages/warnings-original.md)  [warnings-patched](packages/invenio-pages/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-pidstore` <br/>  [original](packages/invenio-pidstore/test-output-original.txt)  [patched](packages/invenio-pidstore/test-output-patched.txt)  [warnings-original](packages/invenio-pidstore/warnings-original.md)  [warnings-patched](packages/invenio-pidstore/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-previewer` <br/>  [patched](packages/invenio-previewer/test-output-patched.txt)  [warnings-patched](packages/invenio-previewer/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-queues` <br/>  [original](packages/invenio-queues/test-output-original.txt)  [patched](packages/invenio-queues/test-output-patched.txt)  [warnings-original](packages/invenio-queues/warnings-original.md)  [warnings-patched](packages/invenio-queues/warnings-patched.md) | pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-rdm-records` <br/>  [original](packages/invenio-rdm-records/test-output-original.txt)  [patched](packages/invenio-rdm-records/test-output-patched.txt)  [warnings-original](packages/invenio-rdm-records/warnings-original.md)  [warnings-patched](packages/invenio-rdm-records/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-records-files` <br/>  [original](packages/invenio-records-files/test-output-original.txt)  [patched](packages/invenio-records-files/test-output-patched.txt)  [warnings-original](packages/invenio-records-files/warnings-original.md)  [warnings-patched](packages/invenio-records-files/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-permissions` <br/>  [patched](packages/invenio-records-permissions/test-output-patched.txt)  [warnings-patched](packages/invenio-records-permissions/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-resources` <br/>  [original](packages/invenio-records-resources/test-output-original.txt)  [patched](packages/invenio-records-resources/test-output-patched.txt)  [warnings-original](packages/invenio-records-resources/warnings-original.md)  [warnings-patched](packages/invenio-records-resources/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-rest` <br/>  [patched](packages/invenio-records-rest/test-output-patched.txt)  [warnings-patched](packages/invenio-records-rest/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-ui` <br/>  [patched](packages/invenio-records-ui/test-output-patched.txt)  [warnings-patched](packages/invenio-records-ui/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records` <br/>  [original](packages/invenio-records/test-output-original.txt)  [patched](packages/invenio-records/test-output-patched.txt)  [warnings-original](packages/invenio-records/warnings-original.md)  [warnings-patched](packages/invenio-records/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-requests` <br/>  [original](packages/invenio-requests/test-output-original.txt)  [patched](packages/invenio-requests/test-output-patched.txt)  [warnings-original](packages/invenio-requests/warnings-original.md)  [warnings-patched](packages/invenio-requests/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-rest` <br/>  [original](packages/invenio-rest/test-output-original.txt)  [patched](packages/invenio-rest/test-output-patched.txt)  [warnings-original](packages/invenio-rest/warnings-original.md)  [warnings-patched](packages/invenio-rest/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-search-ui` <br/>  [patched](packages/invenio-search-ui/test-output-patched.txt)  [warnings-patched](packages/invenio-search-ui/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-search` <br/>  [patched](packages/invenio-search/test-output-patched.txt)  [warnings-patched](packages/invenio-search/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-sitemap` <br/>  [patched](packages/invenio-sitemap/test-output-patched.txt)  [warnings-patched](packages/invenio-sitemap/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-stats` <br/>  [original](packages/invenio-stats/test-output-original.txt)  [patched](packages/invenio-stats/test-output-patched.txt)  [warnings-original](packages/invenio-stats/warnings-original.md)  [warnings-patched](packages/invenio-stats/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-theme` <br/>  [original](packages/invenio-theme/test-output-original.txt)  [patched](packages/invenio-theme/test-output-patched.txt)  [warnings-original](packages/invenio-theme/warnings-original.md)  [warnings-patched](packages/invenio-theme/warnings-patched.md) | pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-userprofiles` <br/>  [patched](packages/invenio-userprofiles/test-output-patched.txt)  [warnings-patched](packages/invenio-userprofiles/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-users-resources` <br/>  [original](packages/invenio-users-resources/test-output-original.txt)  [patched](packages/invenio-users-resources/test-output-patched.txt)  [warnings-original](packages/invenio-users-resources/warnings-original.md)  [warnings-patched](packages/invenio-users-resources/warnings-patched.md) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-vocabularies` <br/>  [patched](packages/invenio-vocabularies/test-output-patched.txt)  [warnings-patched](packages/invenio-vocabularies/warnings-patched.md) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` <br/>  [original](packages/invenio-webhooks/test-output-original.txt)  [patched](packages/invenio-webhooks/test-output-patched.txt)  [warnings-original](packages/invenio-webhooks/warnings-original.md)  [warnings-patched](packages/invenio-webhooks/warnings-patched.md) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |

## Collected Warnings

### Original

#### Warning 1 - 24 occurrences

blah

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-app` | 1 |
| `invenio-app-rdm` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-base` | 1 |
| `invenio-communities` | 1 |
| `invenio-config` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-indexer` | 1 |
| `invenio-jsonschemas` | 1 |
| `invenio-oaiserver` | 1 |
| `invenio-pages` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-queues` | 1 |
| `invenio-rdm-records` | 1 |
| `invenio-records` | 1 |
| `invenio-records-files` | 1 |
| `invenio-records-resources` | 1 |
| `invenio-requests` | 1 |
| `invenio-rest` | 1 |
| `invenio-stats` | 1 |
| `invenio-theme` | 1 |
| `invenio-users-resources` | 1 |
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
