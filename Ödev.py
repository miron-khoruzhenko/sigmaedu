{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "2829d989-0a36-4d01-8b46-0f79263002e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def yuze_kadar_say():\n",
    "\n",
    "    for i in range(0,10):\n",
    "        \n",
    "        for a in range(10):\n",
    "            \n",
    "            sayi = \"{}{}\".format(i,a)\n",
    "            \n",
    "            if a > i:\n",
    "                \n",
    "                if a == 9 and i == 8:\n",
    "                    print(sayi)\n",
    "                    \n",
    "                else:\n",
    "                    print(sayi,end=\",\")\n",
    "            \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "c74bd950-5094-4220-808f-71921629b4f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "01,02,03,04,05,06,07,08,09,12,13,14,15,16,17,18,19,23,24,25,26,27,28,29,34,35,36,37,38,39,45,46,47,48,49,56,57,58,59,67,68,69,78,79,89\n"
     ]
    }
   ],
   "source": [
    "yuze_kadar_say()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af1b754c-8d21-447a-8ce6-842b364d1cca",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 's' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/v2/x_3_ld0j04v8vffknfsctfjm0000gn/T/ipykernel_5413/1028141915.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0ms\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 's' is not defined"
     ]
    }
   ],
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
