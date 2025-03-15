{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e80ada7-cdcf-44bd-850d-852b9516174f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from risk_model import calculate_risk_score\n",
    "\n",
    "risk_score = calculate_risk_score(0.2, 0.3, 0.8, 0.7)\n",
    "print(f\"Test Risk Score: {risk_score}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
