from fastapi import FastAPI
# Note: When running from root, use absolute imports
from app.services.tax_engine import calculate_tax_with_relief 

app = FastAPI(title="Gov&Me Tax Portal")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tax & Subsidy Visualizer"}

@app.post("/services/tax_engine")
def get_tax(taxable_income: float, is_salaried: bool=True):
    # This calls your logic from services/tax_engine.py
    result = calculate_tax_with_relief(taxable_income, is_salaried)
    return {"tax_details": result}
