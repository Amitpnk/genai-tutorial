# Northwind Analytics — Product Handbook

*Fictional company, written for the tutorial. Every fact here is invented so
you can test retrieval and grounding without needing a real corpus.*

## 1. What Northwind Analytics is

Northwind Analytics is a hosted event-analytics platform. Customers send
product events over HTTP or through one of our SDKs, and we store, aggregate,
and visualise them. The three surfaces customers interact with are the
Dashboard (a web app), the Query API (REST + SQL), and the Warehouse Sync
(scheduled exports into the customer's own data warehouse).

We serve roughly 4,200 paying organisations. The largest single account sends
about 1.1 billion events per month; the median account sends 3.4 million.

## 2. Plans and pricing

There are four plans. All prices are per organisation per month, billed in USD.

| Plan | Price | Included events / month | Data retention | Seats |
|---|---|---|---|---|
| Free | $0 | 100,000 | 30 days | 3 |
| Starter | $99 | 2,000,000 | 6 months | 10 |
| Growth | $499 | 20,000,000 | 24 months | 50 |
| Enterprise | Custom | Negotiated | Up to 7 years | Unlimited |

Overage on Starter and Growth is billed at $0.28 per 100,000 events. Free plan
accounts are hard-capped: once the 100,000-event ceiling is reached, further
events are rejected with HTTP 429 until the next billing period. There is no
overage billing on Free.

Annual contracts receive a 15% discount. Annual customers who exceed their
included volume by more than 40% in two consecutive months are contacted for a
mid-term plan upgrade; we do not auto-upgrade anyone.

## 3. Refunds and cancellation

Customers may cancel at any time from Settings → Billing. Cancellation takes
effect at the end of the current billing period; we do not prorate partial
months on monthly plans.

Our refund window is **30 days** from the date of the charge. Within that
window, support can issue a full refund without approval. Beyond 30 days,
refunds require a manager's sign-off and are granted only where there was a
service failure — a documented incident affecting the customer's region, or a
billing error on our side.

Annual contracts are refundable on a prorated basis within the first 60 days.
After 60 days, annual contracts are not refundable, though we will credit the
unused portion toward a renewal if the customer stays.

## 4. Authentication and SSO

Every plan supports API keys, scoped either to ingest (write-only) or query
(read-only). Keys are shown once at creation and stored hashed; a lost key
cannot be recovered, only rotated.

Single sign-on is available on Growth and Enterprise. We support **SAML 2.0**
with any compliant identity provider; Okta, Entra ID, and Google Workspace are
tested on every release. SCIM user provisioning is Enterprise-only. OpenID
Connect is not currently supported — it has been on the roadmap since Q2 and
has no committed date.

Enforcing SSO for an organisation disables password login for every member
except the designated break-glass account, which is exempt by design so an
IdP outage cannot lock an org out entirely.

## 5. Data residency

Data is stored in one of three regions, chosen at organisation creation and
immutable afterwards: `us-east`, `eu-west`, and `ap-south`. Moving an existing
organisation between regions requires a migration ticket and roughly 48 hours
of coordination; during the migration the account is read-only.

EU customers on Growth and Enterprise can additionally enable Strict Residency,
which pins all processing — including our internal batch jobs — to `eu-west`.
Strict Residency disables two features: Warehouse Sync to non-EU destinations,
and the anomaly-detection service, which currently runs only in `us-east`.

## 6. Ingest limits

The ingest endpoint accepts batches of up to 1,000 events or 5 MB, whichever is
smaller. Individual events are capped at 32 KB. Events carrying a timestamp
more than 72 hours in the past are accepted but flagged as late-arriving, and
they do not trigger real-time alerts.

Rate limits are per API key: 500 requests per second on Growth, 100 on Starter,
20 on Free. Enterprise limits are negotiated. Exceeding the limit returns HTTP
429 with a `retry-after` header; our SDKs honour it automatically with
exponential backoff, but direct HTTP integrations must handle it themselves.

## 7. Query API

The Query API accepts a restricted SQL dialect. Joins are permitted only
against the customer's own datasets, and every query is implicitly scoped to
the organisation — there is no way to express a cross-organisation query, which
is the main reason we allow SQL at all.

Queries time out at 60 seconds on Starter and Growth, and 300 seconds on
Enterprise. Results are capped at 100,000 rows; larger result sets must go
through Warehouse Sync instead. Query results are cached for 5 minutes keyed on
the exact query text, so a dashboard refreshing every minute costs one query
execution, not five.

## 8. Warehouse Sync

Warehouse Sync exports raw or aggregated events to Snowflake, BigQuery,
Redshift, or an S3-compatible bucket. It runs on a schedule — hourly at the
fastest, daily by default. Sub-hourly sync is not supported; customers asking
for streaming exports are directed to the ingest webhook fan-out instead.

Sync failures retry three times with backoff. After three failures the sync is
paused and the organisation's owners are emailed. A paused sync must be
resumed manually — we deliberately do not auto-resume, because the usual cause
is a credential or schema change that will keep failing until a human looks.

## 9. Support and SLAs

| Plan | First response | Channel | Uptime SLA |
|---|---|---|---|
| Free | Best effort | Community forum | None |
| Starter | 2 business days | Email | 99.5% |
| Growth | 8 business hours | Email + chat | 99.9% |
| Enterprise | 1 hour (P1) | Email, chat, shared Slack | 99.95% |

SLA credits are 10% of the monthly fee per 0.1% below target, capped at 50% of
the monthly fee. Credits must be requested within 30 days of the incident;
we do not apply them automatically, a policy customers complain about
regularly and which is under review.

## 10. Known limitations

Event property names are limited to 512 distinct keys per organisation.
Exceeding this silently drops new keys rather than erroring — the most common
source of support tickets, and the fix (a hard error plus a dashboard warning)
is scheduled but unreleased.

Timezone handling in scheduled reports uses the organisation's timezone, not
the individual viewer's, which surprises distributed teams. There is no
per-user override.

Deleting a dataset is immediate and irreversible. There is no trash or undo.
