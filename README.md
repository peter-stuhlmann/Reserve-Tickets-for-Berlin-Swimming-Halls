# Reserve time slot tickets for Berlin Swimming Halls

During the Corona pandemic, you have to book tickets online in advance to visit a swimming hall operated by _Berliner Bäderbetriebe_. Since the amount of available tickets for each time slot is low and the demand is sometimes very high, you have to be extremely fast to get a ticket. Tickets are often fully booked within 1-2 seconds after the start of the presale for the respective time slot.   

This simple Python script facilitates the reservation process. It opens the website in the Chrome browser and selects the desired amount of tickets and adds them to the shopping cart. Then you have up to 30 minutes to complete the booking process manually until the purchase.

The following parameters have to be adjusted manually in the script:
- Booking page URL (varies depending on date, time slot and location)
- Amount of tickets
- ID of the corresponding input field element

The script can then be executed via the Windows Task Scheduler at a specific time.

Good luck! :)

