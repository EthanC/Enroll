import logging
from datetime import datetime
from os import environ
from sys import exit, stdout

import dotenv
from discord_webhook import DiscordEmbed, DiscordWebhook
from loguru import logger
from loguru_discord import DiscordSink

from handlers.indexers import (
    NZBCORE,
    DOGnzb,
    DrunkenSlug,
    Indexer,
    NewzBay,
    NewzBurners,
    NinjaCentral,
    NZBCat,
    TabulaRasa,
    omgwtfnzbs,
)
from handlers.intercept import Intercept


def Start() -> None:
    """Initialize Enroll and begin primary functionality."""

    logger.info("Enroll")
    logger.info("https://github.com/EthanC/Enroll")

    # Reroute standard logging to Loguru
    logging.basicConfig(handlers=[Intercept()], level=0, force=True)

    if dotenv.load_dotenv():
        logger.success("Loaded environment variables")
        logger.trace(f"{environ=}")

    if level := environ.get("LOG_LEVEL"):
        logger.remove()
        logger.add(stdout, level=level)

        logger.success(f"Set console logging level to {level}")

    if url := environ.get("LOG_DISCORD_WEBHOOK_URL"):
        logger.add(
            DiscordSink(url),
            level=environ["LOG_DISCORD_WEBHOOK_LEVEL"],
            backtrace=False,
        )

        logger.success("Enabled logging to Discord webhook")
        logger.trace(f"{url=}")

    count: int = 0

    if environ.get("INDEXER_DOGNZB"):
        count += 1

        if result := DOGnzb():
            Notify(result)

    if environ.get("INDEXER_DRUNKENSLUG"):
        count += 1

        if result := DrunkenSlug():
            Notify(result)

    if environ.get("INDEXER_NEWZBAY"):
        count += 1

        if result := NewzBay():
            Notify(result)

    if environ.get("INDEXER_NEWZBURNERS"):
        count += 1

        if result := NewzBurners():
            Notify(result)

    if environ.get("INDEXER_NZBCAT"):
        count += 1

        if result := NZBCat():
            Notify(result)

    if environ.get("INDEXER_NZBCORE"):
        count += 1

        if result := NZBCORE():
            Notify(result)

    if environ.get("INDEXER_NINJACENTRAL"):
        count += 1

        if result := NinjaCentral():
            Notify(result)

    if environ.get("INDEXER_OMGWTFNZBS"):
        count += 1

        if result := omgwtfnzbs():
            Notify(result)

    if environ.get("INDEXER_TABULARASA"):
        count += 1

        if result := TabulaRasa():
            Notify(result)

    logger.success(
        f"Completed {count:,} Indexer registration availability {"check" if count == 1 else "checks"}"
    )


def Notify(indexer: Indexer) -> None:
    """Report registration availability to the configured Discord webhook."""

    if not (url := environ.get("DISCORD_WEBHOOK_URL")):
        logger.info("Discord webhook for notifications is not set")

        return

    embed: DiscordEmbed = DiscordEmbed()

    embed.set_color(indexer.color)
    embed.set_author(indexer.name, url=indexer.home, icon_url=indexer.icon)
    embed.set_description(
        f"{indexer.name} is now open for [registration]({indexer.register})."
    )

    embed.set_footer("Enroll", icon_url="https://i.imgur.com/eEJ8gSt.png")  # pyright: ignore [reportUnknownMemberType]
    embed.set_timestamp(datetime.now().timestamp())

    DiscordWebhook(url, embeds=[embed], rate_limit_retry=True).execute()


if __name__ == "__main__":
    try:
        Start()
    except KeyboardInterrupt:
        exit()
