import httpx
from httpx import Response
from loguru import logger


class Indexer:
    """Generic class containing Indexer information."""

    def __init__(
        self, name: str, home: str, register: str, color: str, icon: str
    ) -> None:
        """Initialize an Indexer object."""

        self.name: str = name
        self.home: str = home
        self.register: str = register
        self.color: str = color
        self.icon: str = icon


def _Request(indexer: Indexer, allow: list[int] = []) -> str | None:
    """Safely perform an HTTP request and return the response if available."""

    logger.debug(f"Checking registration availability of {indexer.name}...")
    logger.trace(indexer)

    request: Response | None = None

    try:
        request = httpx.get(indexer.register)

        request.raise_for_status()

        if not request:
            raise RuntimeError("request object is null")
    except Exception as e:
        if (not request) or (request.status_code not in allow):
            logger.opt(exception=e).error(
                f"Failed to determine Indexer {indexer.name} registration availability"
            )

            return

    logger.trace(f"{request.text=}")

    return request.text


def DOGnzb() -> Indexer | None:
    """Determine registration availability for DOGznb."""

    meta = Indexer(
        "DOGnzb",
        "https://dognzb.cr/login",
        "https://dognzb.cr/register",
        "009900",
        "https://i.imgur.com/pGW2IXb.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "We understand your desire to check if registrations are open.
        # But excessive hammering is not tolerated and your IP address
        # has been blacklisted. Limit your registration checks to
        # reasonable intervals and the restriction will lift automatically."
        if "blacklisted" in data.lower():
            logger.warning(f"Indexer {meta.name} ratelimited registration check")

            return
        else:
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")


def DrunkenSlug() -> Indexer | None:
    """Determine registration availability for DrunkenSlug."""

    meta = Indexer(
        "DrunkenSlug",
        "https://drunkenslug.com/login",
        "https://drunkenslug.com/register",
        "FFA500",
        "https://drunkenslug.com/themes/shared/img/welcome.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "Sorry! The Bar is closed.
        # Please don't contact us asking for invites.""
        if not "bar is closed" in data.lower():
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")

    return meta


def NewzBay() -> Indexer | None:
    """Determine registration availability for NewzBay."""

    meta = Indexer(
        "NewzBay",
        "https://newzbay.cc/",
        "https://newzbay.cc/register",
        "F9D459",
        "https://newzbay.cc/templates/index/favicon/android-chrome-192x192.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "Registrations are currently invite only.""
        if not "invite only" in data.lower():
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")


def NZBCat() -> Indexer | None:
    """Determine registration availability for NZB.Cat."""

    meta = Indexer(
        "NZB.Cat",
        "https://nzb.cat/",
        "https://nzb.cat/register",
        "337AB7",
        "https://i.imgur.com/LoJ9yF2.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "Registrations are currently invite only."
        if not "invite only" in data.lower():
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")


def NZBsin() -> Indexer | None:
    """Determine registration availability for NZBs.in (formerly NewzBurnerz)."""

    meta = Indexer(
        "NZBs.in",
        "https://v2.nzbs.in/login",
        "https://v2.nzbs.in/register",
        "6CFFF0",
        "https://i.imgur.com/avY6azl.png",
    )
    data: str | None = _Request(meta, [403])

    if data:
        # "Important: Server Downtime and Migration Update"
        if "server downtime" in data.lower():
            logger.info(f"Indexer {meta.name} is currently undergoing maintenance")

            return
        # "Registration is currently closed."
        # "Registration is by invitation only."
        elif (not "currently closed" in data.lower()) and (
            not "invitation only" in data.lower()
        ):
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")


def NZBCORE() -> Indexer | None:
    """Determine registration availability for NZBCORE."""

    meta = Indexer(
        "NZBCORE",
        "https://nzbcore.info/nnplus/www/",
        "https://nzbcore.info/nnplus/www/register",
        "638700",
        "https://nzbcore.info/nnplus/www/templates/bookstrap/images/hydra-nzbcore5.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "Registrations are currently disabled."
        if not "currently disabled" in data.lower():
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")


def NinjaCentral() -> Indexer | None:
    """Determine registration availability for NinjaCentral."""

    meta = Indexer(
        "NinjaCentral",
        "https://ninjacentral.co.za/",
        "https://ninjacentral.co.za/register",
        "242C45",
        "https://ninjacentral.co.za/templates/ninja/images/NC_Logo.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "Registrations are currently disabled."
        if not "currently disabled" in data.lower():
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")


def omgwtfnzbs() -> Indexer | None:
    """Determine registration availability for omgwtfnzbs."""

    meta = Indexer(
        "omgwtfnzbs",
        "https://omgwtfnzbs.org/login",
        "https://omgwtfnzbs.org/register",
        "16CE16",
        "https://omgwtfnzbs.org/apple-touch-icon-180x180.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "Stop trying stuff .. banned!"
        if "banned" in data.lower():
            logger.warning(f"Indexer {meta.name} ratelimited registration check")

            return
        # "Public Registrations have been disabled by the site admin"
        elif not "site admin" in data.lower():
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")


def TabulaRasa() -> Indexer | None:
    """Determine registration availability for Tabula Rasa."""

    meta = Indexer(
        "Tabula Rasa",
        "https://www.tabula-rasa.pw/login",
        "https://www.tabula-rasa.pw/register",
        "ECF0F1",
        "https://i.imgur.com/VUDBpu0.png",
    )
    data: str | None = _Request(meta)

    if data:
        # "Registrations are currently closed."
        if not "currently closed" in data.lower():
            logger.success(f"Indexer {meta.name} registration is open")

            return meta

    logger.info(f"Indexer {meta.name} registration is closed")
