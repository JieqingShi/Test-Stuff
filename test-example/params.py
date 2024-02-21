# don't forget to set wandb api key in secrets
WANDB_PROJECT = "wandb-cicd-course"
ENTITY = 'jieqingshi'
BDD_CLASSES = {i:c for i,c in enumerate(['background', 'road', 'traffic light', 'traffic sign', 'person', 'vehicle', 'bicycle'])}
RAW_DATA_AT = 'av-team/mlops-course-001/bdd_simple_1k'
PROCESSED_DATA_AT = 'av-team/mlops-course-001/bdd_simple_1k_split'
