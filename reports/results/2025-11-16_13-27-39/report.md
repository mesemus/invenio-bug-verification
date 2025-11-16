# Invenio Bugfix Verification Results

_Last updated: 2025-11-16 13:27:39 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 52 |
| **Patched Packages** | 51 |
| **Unpatched Packages** | 1 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 6 |
| ⚠️  Still Failing | 4 |
| ℹ️  No Change | 41 |

## 🔧 Configured Patches

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-db` <br/>  [patched](packages/invenio-db/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `null` | ❓ Unknown |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-access` <br/>  [patched](packages/invenio-access/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-accounts` <br/>  [patched](packages/invenio-accounts/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-administration` <br/>  [patched](packages/invenio-administration/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-app-rdm` <br/>  [patched](packages/invenio-app-rdm/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-app` <br/>  [patched](packages/invenio-app/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-assets` <br/>  [patched](packages/invenio-assets/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` <br/>  [patched](packages/invenio-audit-logs/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-banners` <br/>  [original](packages/invenio-banners/test-output-original.txt)  [patched](packages/invenio-banners/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-base` <br/>  [patched](packages/invenio-base/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-cache` <br/>  [patched](packages/invenio-cache/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-celery` <br/>  [patched](packages/invenio-celery/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-checks` <br/>  [patched](packages/invenio-checks/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-collections` <br/>  [patched](packages/invenio-collections/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-communities` <br/>  [original](packages/invenio-communities/test-output-original.txt)  [patched](packages/invenio-communities/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-config` <br/>  [patched](packages/invenio-config/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-db` <br/>  [patched](packages/invenio-db/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` <br/>  [patched](packages/invenio-drafts-resources/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-files-rest` <br/>  [original](packages/invenio-files-rest/test-output-original.txt)  [patched](packages/invenio-files-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-formatter` <br/>  [patched](packages/invenio-formatter/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-github` <br/>  [original](packages/invenio-github/test-output-original.txt)  [patched](packages/invenio-github/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-i18n` <br/>  [patched](packages/invenio-i18n/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` <br/>  [patched](packages/invenio-indexer/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` <br/>  [original](packages/invenio-jobs/test-output-original.txt)  [patched](packages/invenio-jobs/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-jsonschemas` <br/>  [patched](packages/invenio-jsonschemas/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-logging` <br/>  [patched](packages/invenio-logging/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-mail` <br/>  [patched](packages/invenio-mail/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` <br/>  [patched](packages/invenio-notifications/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oaiserver` <br/>  [patched](packages/invenio-oaiserver/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oauth2server` <br/>  [patched](packages/invenio-oauth2server/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-oauthclient` <br/>  [patched](packages/invenio-oauthclient/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-pages` <br/>  [patched](packages/invenio-pages/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` <br/>  [patched](packages/invenio-pidstore/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-previewer` <br/>  [patched](packages/invenio-previewer/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-queues` <br/>  [patched](packages/invenio-queues/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-files` <br/>  [original](packages/invenio-records-files/test-output-original.txt)  [patched](packages/invenio-records-files/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-permissions` <br/>  [patched](packages/invenio-records-permissions/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-resources` <br/>  [patched](packages/invenio-records-resources/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-rest` <br/>  [patched](packages/invenio-records-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-ui` <br/>  [patched](packages/invenio-records-ui/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records` <br/>  [original](packages/invenio-records/test-output-original.txt)  [patched](packages/invenio-records/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-requests` <br/>  [patched](packages/invenio-requests/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-rest` <br/>  [patched](packages/invenio-rest/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-search-ui` <br/>  [patched](packages/invenio-search-ui/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-search` <br/>  [original](packages/invenio-search/test-output-original.txt)  [patched](packages/invenio-search/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-sitemap` <br/>  [patched](packages/invenio-sitemap/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-stats` <br/>  [original](packages/invenio-stats/test-output-original.txt)  [patched](packages/invenio-stats/test-output-patched.txt) | invenio-db pytest-invenio  | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-theme` <br/>  [patched](packages/invenio-theme/test-output-patched.txt) | pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-userprofiles` <br/>  [patched](packages/invenio-userprofiles/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-users-resources` <br/>  [original](packages/invenio-users-resources/test-output-original.txt)  [patched](packages/invenio-users-resources/test-output-patched.txt) | invenio-db pytest-invenio  | ✅ Pass | ❌ Fail | ❌ Patch introduced test failures |
| `invenio-vocabularies` <br/>  [patched](packages/invenio-vocabularies/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` <br/>  [patched](packages/invenio-webhooks/test-output-patched.txt) | invenio-db pytest-invenio  | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## Collected Warnings

No warnings found in any package.
---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._
