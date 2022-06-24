from ml_collections import ConfigDict

from experiment_configs.default import get_config as default_config


def get_config():
    cfg = default_config()
    cfg.tasks.list = [
        {
            'task': 'forecasting',
            'freeze_featurizer': True,
        },
        {
            'task': 'classification',
            'run': 'forecasting>classification'
        }
    ]
    cfg.tasks.list = [ConfigDict(d) for d in cfg.tasks.list]
    cfg.project = 'feature-freeze'
    return cfg