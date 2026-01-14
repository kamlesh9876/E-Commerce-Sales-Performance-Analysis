# E-Commerce Data Dictionary

## Overview
This document defines the expected data structure and field descriptions for the e-commerce sales analysis project.

## Tables Structure

### 1. Orders Table
| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| order_id | String/Integer | Unique identifier for each order | ORD-001 |
| customer_id | String/Integer | Foreign key to customers table | CUST-123 |
| product_id | String/Integer | Foreign key to products table | PROD-456 |
| order_date | DateTime | Date and time when order was placed | 2024-01-15 14:30:00 |
| quantity | Integer | Number of units ordered | 2 |
| unit_price | Decimal | Price per unit before discount | 29.99 |
| total_amount | Decimal | Total order value (quantity × unit_price - discount) | 59.98 |
| discount_amount | Decimal | Discount applied to order | 5.00 |
| discount_percentage | Decimal | Discount percentage applied | 8.33 |
| status | String | Order status | 'completed', 'cancelled', 'pending', 'returned' |
| payment_method | String | Payment method used | 'credit_card', 'paypal', 'cash_on_delivery' |
| shipping_address | Text | Complete shipping address | '123 Main St, City, State' |
| shipping_cost | Decimal | Cost of shipping | 4.99 |
| tax_amount | Decimal | Tax applied to order | 4.80 |
| created_at | DateTime | Timestamp when record was created | 2024-01-15 14:30:00 |
| updated_at | DateTime | Timestamp when record was last updated | 2024-01-15 14:35:00 |

### 2. Products Table
| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| product_id | String/Integer | Unique identifier for each product | PROD-456 |
| product_name | String | Name of the product | 'Wireless Bluetooth Headphones' |
| category | String | Main product category | 'Electronics' |
| subcategory | String | Product subcategory | 'Audio' |
| brand | String | Product brand | 'TechBrand' |
| sku | String | Stock Keeping Unit | TB-WH-001 |
| price | Decimal | Selling price | 29.99 |
| cost | Decimal | Cost to business | 15.50 |
| profit_margin | Decimal | Profit margin percentage | 48.3 |
| stock_quantity | Integer | Current inventory level | 150 |
| reorder_level | Integer | Minimum stock before reordering | 20 |
| weight | Decimal | Product weight in kg | 0.5 |
| dimensions | String | Product dimensions | '20x15x5 cm' |
| description | Text | Product description | 'High-quality wireless headphones...' |
| created_date | DateTime | Date product was added to catalog | 2024-01-01 00:00:00 |
| last_updated | DateTime | Last update timestamp | 2024-01-10 10:30:00 |
| is_active | Boolean | Whether product is currently active | True |

### 3. Customers Table
| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| customer_id | String/Integer | Unique identifier for each customer | CUST-123 |
| first_name | String | Customer first name | 'John' |
| last_name | String | Customer last name | 'Doe' |
| email | String | Customer email address | 'john.doe@email.com' |
| phone | String | Customer phone number | '+1-555-0123' |
| gender | String | Customer gender | 'Male', 'Female', 'Other' |
| birth_date | Date | Customer date of birth | 1990-05-15 |
| address | Text | Street address | '123 Main St, Apt 4B' |
| city | String | City | 'New York' |
| state | String | State/Province | 'NY' |
| country | String | Country | 'USA' |
| postal_code | String | Postal/ZIP code | '10001' |
| registration_date | DateTime | When customer account was created | 2023-06-15 09:00:00 |
| last_purchase_date | DateTime | Date of most recent purchase | 2024-01-10 14:20:00 |
| total_purchases | Decimal | Total amount spent by customer | 1250.75 |
| order_count | Integer | Total number of orders placed | 8 |
| customer_segment | String | Customer segmentation | 'VIP', 'Regular', 'New', 'Inactive' |
| loyalty_points | Integer | Customer loyalty points balance | 450 |
| preferred_payment | String | Preferred payment method | 'credit_card' |
| marketing_consent | Boolean | Consent for marketing communications | True |

## Data Quality Standards

### Required Fields
- All ID fields must be unique and non-null
- Order dates must be valid timestamps
- Quantities must be positive integers
- Prices and amounts must be positive decimals

### Data Validation Rules
- Email addresses must follow standard format
- Phone numbers must follow country-specific format
- Postal codes must match country format
- Order status must be one of: 'completed', 'cancelled', 'pending', 'returned', 'processing'

### Expected Data Volume
- Orders: 10,000 - 1,000,000 records
- Products: 100 - 10,000 records  
- Customers: 1,000 - 100,000 records

## Data Sources
This data typically comes from:
- E-commerce platform database (Shopify, Magento, WooCommerce)
- Order management system
- Inventory management system
- Customer relationship management (CRM) system
- Payment gateway records

## Privacy Considerations
- Customer PII (Personally Identifiable Information) should be anonymized for analysis
- Payment information should be tokenized or removed
- Address data may be generalized to city/country level for broader analysis
