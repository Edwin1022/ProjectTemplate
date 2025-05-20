echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.12"
conda create --prefix ./env python=3.12 -y
echo [$(date)]: "Activating conda env"
source $(conda info --base)/etc/profile.d/conda.sh
conda activate ./env
echo [$(date)]: "Installing requirements"
pip install -r requirements.txt
echo [$(date)]: "END"