package com.kuronami.frozenworld;

import com.kuronami.isekaiapi.api.Isekai;
import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

@Mod(FrozenWorld.MODID)
public final class FrozenWorld {
    public static final String MODID = "frozen_world";
    public static final String VERSION = "1.1.0";
    public static final Logger LOGGER = LogUtils.getLogger();

    public FrozenWorld(IEventBus modBus) {
        LOGGER.info("Frozen World v{} loading", VERSION);
        LOGGER.info("Frozen World: Isekai API facade ready (query={}, remap={})",
                Isekai.query().getClass().getSimpleName(),
                Isekai.remap().getClass().getSimpleName());
    }
}
