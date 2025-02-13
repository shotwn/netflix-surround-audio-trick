import asyncio
import os
from winrt.windows.media.audio import SpatialAudioDeviceConfiguration, SpatialAudioFormatSubtype
from winrt.windows.media.devices import MediaDevice

DOLBY_ATMOS_HEADPHONES = SpatialAudioFormatSubtype.dolby_atmos_for_headphones

async def main():
    default_playback_device_id = MediaDevice.get_default_audio_render_id(0)
    spatial_audio_device_configuration = SpatialAudioDeviceConfiguration.get_for_device_id(default_playback_device_id)
    
    if is_dolby_atmos_enabled(spatial_audio_device_configuration):
        print("Dolby Atmos for Headphones is already enabled")
    else:
        print("Dolby Atmos for Headphones is not enabled")
        await spatial_audio_device_configuration.set_default_spatial_audio_format_async(DOLBY_ATMOS_HEADPHONES)
        if is_dolby_atmos_enabled(spatial_audio_device_configuration):
            print("Dolby Atmos for Headphones has been enabled")
        else:
            print("Failed to enable Dolby Atmos")
            await asyncio.sleep(600)
            return
        
    # Start netflix uwp
    os.system("start shell:AppsFolder\\4DF9E0F8.Netflix_mcm4njqhnhss8!Netflix.App")

    # Wait for 10 seconds
    sleep_timer = 10
    for i in range(sleep_timer):
        if i > 0:
            # Remove last line on console
            print("\033[A                             \033[A")
            
        print(f"Waiting for {sleep_timer - i} seconds...")
        
        await asyncio.sleep(1)

    # Disable Dolby Atmos Headphones
    await spatial_audio_device_configuration.set_default_spatial_audio_format_async("{00000000-0000-0000-0000-000000000000}")

    if is_dolby_atmos_enabled(spatial_audio_device_configuration):
        print("Failed to disable Dolby Atmos for Headphones. You might need to manually disable it.")
        await asyncio.sleep(600)
    else:
        print("Dolby Atmos for Headphones has been disabled")


def is_dolby_atmos_enabled(spatial_audio_device_configuration):
    active_spatial_audio_format = spatial_audio_device_configuration.active_spatial_audio_format

    return active_spatial_audio_format == DOLBY_ATMOS_HEADPHONES


asyncio.run(main())