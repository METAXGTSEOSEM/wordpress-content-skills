# Security policy

## Supported versions

Security reports are accepted for the latest released article Skill and the
current `main` branch. Older releases may not receive fixes.

## What to report

Please report:

- prompt-injection or instruction-escalation paths in Skill files or templates;
- scripts that execute untrusted content, expose credentials or write outside
  the intended workspace;
- workflow or validator bypasses;
- malicious links, unsafe attachments or dependency concerns;
- accidental publication of credentials, private data or customer material.

The article Skill is designed to prepare content, not publish or modify a live
site by default. A report that a page was not published is not a security issue.

## How to report

Do not open a public Issue for a sensitive report. Use the repository's
**Security** tab and choose **Report a vulnerability** so the maintainer can
review it privately. If that option is unavailable, contact the maintainer
through their GitHub profile and ask for a private channel before sharing
details.

Include:

- affected file, version or commit;
- a minimal reproduction;
- the impact and any required preconditions;
- relevant logs with credentials and personal data removed.

Never include live API keys, passwords, customer records or private messages.

## Response

Reports are reviewed on a best-effort basis. There is no guaranteed response or
fix deadline. The maintainer will confirm scope, request missing details when
needed, and avoid claiming a fix before it is verified.

## Scope

This policy covers this repository's Skill files, scripts, templates, workflows
and documentation. Third-party Humanizer projects, model providers, browsers,
hosts and CMS plugins have their own security policies.
