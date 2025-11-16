# alx_travel_app_0x00

## Task 0: Database Modeling and Data Seeding in Django

### Objective
Define core database models, set up API serializers, and implement a custom management command to seed the database with sample travel listings.

---

### Project Structure
- **Repository**: [alx_travel_app_0x00](https://github.com/ekipruto/alx_travel_app_0x00)
- **Directory**: `alx_travel_app`
- **Key Files**:
  - `listings/models.py`
  - `listings/serializers.py`
  - `listings/management/commands/seed.py`
  - `README.md`

---

### Setup Instructions

#### 1. Duplicate Project
Clone and rename the original project `alx_travel_app` to `alx_travel_app_0x00`.

```bash
git clone https://github.com/ekipruto/alx_travel_app_0x00.git
cd alx_travel_app_0x00

2. Create Models
Define the following models in listings/models.py:
- Listing: Travel destination details
- Booking: User reservations
- Review: User feedback and ratings
Ensure proper field types, relationships (e.g., ForeignKey), and constraints
3. Set Up Serializers
In listings/serializers.py, create:
- ListingSerializer
- BookingSerializer
These will format data for API responses.
4. Implement Seeder
Create a custom Django management command in:
listings/management/commands/seed.py


This script should populate the database with sample listings for testing and development.
5. Run Seed Command
Execute the seeder to populate your database:
python manage.py seed
