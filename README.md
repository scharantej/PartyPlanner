## Design for a Flask Application to Plan a Birthday Party

## HTML Files

### index.html
- The home page, where users can input the date and time of the party, the number of attendees, and any special requests.
- The page should include HTML form elements for user inputs and a submit button.

### guest_list.html
- Displays the list of guests who have RSVP'd to the party.
- Should include a table to display the guest names, email addresses, and any special requests.

### invitations.html
- Page for sending email invitations to guests.
- Should include a form with fields for guest email addresses, a subject line, and the invitation message.

## Routes

### '/' (GET)
- Renders the index.html page.

### '/guest_list' (GET)
- Queries the database for the list of guests who have RSVP'd.
- Renders the guest_list.html page, passing the guest list data.

### '/invitations' (POST)
- Accepts form data from the invitations.html page.
- Sends email invitations to the specified guest email addresses.
- Redirects to the index.html page with a success message.

### '/rsvp' (POST)
- Accepts form data from the index.html page, including guest information and special requests.
- Adds the guest to the database and sends an RSVP confirmation email.
- Redirects to the index.html page with a thank you message.