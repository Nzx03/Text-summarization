import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from src.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.logging import logging
import sys
from src.exception import CustomException
STAGE_NAME="Data Ingestion stage"
try:
    logging.info(f"{STAGE_NAME} started")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f"{STAGE_NAME} completed")

except Exception as e:
    raise CustomException(e,sys)