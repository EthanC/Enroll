# Enroll

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/EthanC/Enroll/ci.yaml?branch=main) ![Docker Pulls](https://img.shields.io/docker/pulls/ethanchrisp/enroll?label=Docker%20Pulls) ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/ethanchrisp/enroll/latest?label=Docker%20Image%20Size)

Enroll monitors Usenet Indexers and notifies about open registrations.

<p align="center">
    <img src="https://i.imgur.com/xA0qxSf.png" draggable="false">
</p>

## Setup

Although not required, a [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) is recommended for notifications.

Regardless of your chosen setup method, Enroll is intended for use with a task scheduler, such as [cron](https://crontab.guru/).

**Environment Variables:**

-   `LOG_LEVEL`: [Loguru](https://loguru.readthedocs.io/en/stable/api/logger.html) severity level to write to the console.
-   `LOG_DISCORD_WEBHOOK_URL`: [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) URL to receive log events.
-   `LOG_DISCORD_WEBHOOK_LEVEL`: Minimum [Loguru](https://loguru.readthedocs.io/en/stable/api/logger.html) severity level to forward to Discord.
-   `DISCORD_WEBHOOK_URL`: [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) URL to receive open registration notifications.
-   `INDEXER_DOGNZB`: Check the Indexer [DOGnzb](https://dognzb.cr/login) for open registration.
-   `INDEXER_DRUNKENSLUG`: Check the Indexer [DrunkenSlug](https://drunkenslug.com/login) for open registration.
-   `INDEXER_NEWZBAY`: Check the Indexer [NewzBay](https://newzbay.cc/) for open registration.
-   `INDEXER_NZBCAT`: Check the Indexer [NZB.Cat](https://nzb.cat/) for open registration.
-   `INDEXER_NZBSIN`: Check the Indexer [NZBs.in](https://v2.nzbs.in/) for open registration.
-   `INDEXER_NZBCORE`: Check the Indexer [NZBCORE](https://nzbcore.info/nnplus/www/) for open registration.
-   `INDEXER_NINJACENTRAL`: Check the Indexer [NinjaCentral](https://ninjacentral.co.za/) for open registration.
-   `INDEXER_OMGWTFNZBS`: Check the Indexer [omgwtfnzbs](https://omgwtfnzbs.org/login) for open registration.
-   `INDEXER_TABULARASA`: Check the Indexer [Tabula Rasa](https://www.tabula-rasa.pw/login) for open registration.

### Docker (Recommended)

Modify the following `compose.yaml` example file, then run `docker compose up`.

```yaml
services:
  enroll:
    container_name: enroll
    image: ethanchrisp/enroll:latest
    environment:
      LOG_LEVEL: INFO
      LOG_DISCORD_WEBHOOK_URL: https://discord.com/api/webhooks/YYYYYYYY/YYYYYYYY
      LOG_DISCORD_WEBHOOK_LEVEL: WARNING
      DISCORD_WEBHOOK_URL: https://discord.com/api/webhooks/XXXXXXXX/XXXXXXXX
      INDEXER_DOGNZB: true
      INDEXER_DRUNKENSLUG: true
      INDEXER_NINJACENTRAL: true
```

### Standalone

Enroll is built for [Python 3.13](https://www.python.org/) or greater.

1. Install required dependencies using [uv](https://github.com/astral-sh/uv): `uv sync`
2. Rename `.env.example` to `.env`, then provide the environment variables.
3. Start Enroll: `python enroll.py`
