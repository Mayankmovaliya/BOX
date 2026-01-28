{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5b05d8ea-4feb-44a8-80b0-3dcd17248b11",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-01-28 14:54:36.263 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\moval\\AppData\\Local\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-01-28 14:54:36.268 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import math\n",
    "\n",
    "st.set_page_config(page_title=\"Box Price Calc\", page_icon=\"📦\")\n",
    "\n",
    "st.title(\"📦 Box Price Calculator\")\n",
    "\n",
    "# Input Fields\n",
    "l = st.number_input(\"Box Length (mm)\", value=590.0)\n",
    "w = st.number_input(\"Box Width (mm)\", value=360.0)\n",
    "h = st.number_input(\"Box Height (mm)\", value=320.0)\n",
    "ply = st.selectbox(\"Number of Ply\", [3, 5, 7, 9], index=1)\n",
    "gsm_input = st.text_input(\"GSM per Ply (separated by commas)\", \"100, 120, 100, 120, 100\")\n",
    "rate = st.number_input(\"Price Rate\", value=60.0)\n",
    "\n",
    "if st.button(\"Calculate\", type=\"primary\"):\n",
    "    try:\n",
    "        gsm_list = [float(x.strip()) for x in gsm_input.split(',')]\n",
    "        \n",
    "        if len(gsm_list) != ply:\n",
    "            st.error(f\"Please enter exactly {ply} GSM values.\")\n",
    "        else:\n",
    "            # Calculation Logic\n",
    "            sheet_l = math.ceil((h + w) / 25.4)\n",
    "            sheet_h = math.ceil((2 * (l + w) + 50) / 25.4)\n",
    "            \n",
    "            multiplier_map = {3: 3.4, 5: 5.8, 7: 8.2, 9: 10.6}\n",
    "            multiplier = multiplier_map.get(ply, 3.4 + (ply - 3) * 1.2)\n",
    "            avg_gsm = sum(gsm_list) / ply\n",
    "            \n",
    "            price = (((sheet_l * sheet_h * multiplier * avg_gsm) / 1550) * rate) / 1000\n",
    "            \n",
    "            # Results\n",
    "            st.success(f\"### Final Price: ₹{price:.2f}\")\n",
    "            st.info(f\"Sheet Size: {sheet_l}\\\" x {sheet_h}\\\" | Avg GSM: {avg_gsm:.2f}\")\n",
    "    except:\n",
    "        st.error(\"Invalid input. Check your numbers and commas.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43be98bb-a3fa-469e-abb0-bd46317540ea",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
