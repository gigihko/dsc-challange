## DSC Challange

### Prerequisites  & Installing


Create conda env:


``
conda create --n openai_env python=3.9
``

Activate env:


``
conda activate openai_env
``

Install All Depedencies :

``
pip install -r requirements.txt
``

Run :

``
uvicorn main:app --reload --log-level debug --port 8200
``