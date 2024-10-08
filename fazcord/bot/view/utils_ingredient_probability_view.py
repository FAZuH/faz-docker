from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING, Any, override

from nextcord import Embed, Interaction

from fazcord.bot.view._base_view import BaseView
from fazcord.bot.view._custom_embed import CustomEmbed
from fazcord.wynn.ingredient_util import IngredientUtil

if TYPE_CHECKING:
    from fazcord.bot.bot import Bot


class UtilsIngredientProbabilityView(BaseView):
    _THUMBNAIL_URL = "https://www.wynndata.tk/assets/images/items/v4//ingredients/heads/50d8ba53402f4cb0455067d068973b3d.png"

    def __init__(
        self,
        bot: Bot,
        interaction: Interaction[Any],
        base_chance: Decimal,
        loot_bonus: int,
        loot_quality: int,
    ) -> None:
        super().__init__(bot, interaction)
        self._base_chance = base_chance
        self._loot_bonus = loot_bonus
        self._loot_quality = loot_quality

        self._ing_util = IngredientUtil(
            self._base_chance, self._loot_quality, self._loot_bonus
        )
        self._embed = CustomEmbed(
            self._interaction,
            title="Ingredient Chance Calculator",
            color=472931,
            thumbnail_url=self._THUMBNAIL_URL,
        )

    @override
    async def run(self) -> None:
        await self._interaction.send(embed=self._get_embed(self._ing_util))

    def _get_embed(self, ing_util: IngredientUtil) -> Embed:
        embed = self._embed.get_base()
        embed.description = (
            f"` Drop Chance  :` **{ing_util.base_probability:.2%}**\n"
            f"` Loot Bonus   :` **{ing_util.loot_bonus}%**\n"
            f"` Loot Quality :` **{ing_util.loot_quality}%**\n"
            f"` Loot Boost   :` **{ing_util.loot_boost}%**"
        )
        one_in_n = 1 / ing_util.boosted_probability
        embed.add_field(
            name="Boosted Drop Chance",
            value=f"**{ing_util.boosted_probability:.2%}** OR **1 in {one_in_n:.2f}** mobs",
        )
        embed.finalize()
        return embed
