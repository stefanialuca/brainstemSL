from brainstem.app import Brainstem
from config import settings

brainstem = Brainstem(settings)


configs = [
    {
        "asset_name": "crash_course",
        "config_path": "assets/crash_course/configs/crash_course_forecast_config.json",
        "config_name": "crash_course_config"
    }
]

if __name__ == '__main__':
    for config in configs:
        brainstem.run_flow(config['asset_name'], config['config_path'], config['config_name'])
