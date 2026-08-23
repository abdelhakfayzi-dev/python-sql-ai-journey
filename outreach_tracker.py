import csv
from datetime import datetime, timedelta
from datetime import date
import os

CSV_FILE = "leads.csv"
file_exists = os.path.isfile(CSV_FILE)
fieldnames = ['Company', 'Contact', 'Email', 'date_sent', 'status', 'follow_up_date', 'notes']

with open(CSV_FILE , mode='a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()
        
def add_lead(company, contact, email):
    date_sent = datetime.now().strftime("%Y-%m-%d")
    follow_up_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            'Company': company,
            'Contact': contact,
            'Email': email,
            'date_sent': date_sent,
            'status': 'sent',
            'follow_up_date': follow_up_date,
            'notes': ''
        })


today = date.today()
def show_follow_ups():
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        rows = csv.DictReader(f)
        found = False
        for row in rows:
            if datetime.strptime(row['follow_up_date'], "%Y-%m-%d").date() <= today and row['status'] == 'sent':
                print(f"Follow up: {row['Company']} — {row['Contact']} — {row['Email']} (due: {row['follow_up_date']})")
                found = True
            
        if not found:
         print('No follow-ups due today.')

    pass

def show_stats():
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        rows = csv.DictReader(f)
        total_count = 0
        replied_count = 0
        sent_count = 0
        for row in rows:
            if row:
                total_count += 1 
                if row['status'] == 'replied':
                    replied_count += 1
                if datetime.strptime(row['follow_up_date'], "%Y-%m-%d").date() <= today and row['status'] == 'sent':
                    sent_count += 1
        reply_rate = (replied_count / total_count * 100) if total_count > 0 else 0
        print("=== STATS ===")
        print(f"Total pitched: {total_count}")
        print(f"Replied: {replied_count}")
        print(f"Follow ups due: {sent_count}")
        print(f"Reply rate: {reply_rate:.1f}%")   
    
def main():
    print("\n=== OUTREACH TRACKER ===")
    print("1. Add lead")
    print("2. Show follow-ups due today")
    print("3. Show stats")
    print("4. Exit")
    
    choice = input("\nChoose: ")
    
    if choice == "1":
        company = input("Company: ")
        contact = input("Contact name: ")
        email = input("Email: ")
        add_lead(company, contact, email)
        print("Lead added.")
    elif choice == "2":
        show_follow_ups()
    elif choice == "3":
        show_stats()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()