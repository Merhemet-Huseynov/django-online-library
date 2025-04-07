### 📄 API Documentation

Below are some key details about the APIs:

---

### **Token-Related Endpoints 🚀🔑:**

#### 1. **Obtain Token (for login)**
- **URL**: `/token/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response (201 - Content-Type: application/json)**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

#### 2. **Refresh Token**
- **URL**: `/token/refresh/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "refresh": "string"
  }
  ```
- **Response (201 - Content-Type: application/json)**:
  ```json
  {
    "refresh": "string",
    "access": "string"
  }
  ```

#### 3. **Verify Token**
- **URL**: `/token/verify/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "token": "string"
  }
  ```
- **Response (201 - Content-Type: application/json)**:
  ```json
  {
    "token": "string"
  }
  ```

---

### **Account Endpoints 👤:**

#### 4. **Change Password**
- **URL**: `/v1/accounts/change-password/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "old_password": "string",
    "new_password": "string",
    "confirm_password": "string"
  }
  ```
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "message": "Password changed successfully."
  }
  ```
- **Response (400 - Content-Type: application/json)**:
  ```json
  {
    "message": "Bad request. Invalid input."
  }
  ```

#### 5. **Reset Password Send Code**
- **URL**: `/v1/accounts/reset-password-send-code/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "username": "string"
  }
  ```
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "message": "Password reset code sent successfully to the email.",
    "email": "user@example.com"
  }
  ```
- **Response (400 - Content-Type: application/json)**:
  ```json
  {
    "message": "Invalid username."
  }
  ```

#### 6. **Reset Password**
- **URL**: `/v1/accounts/reset-password/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "username": "string",
    "verification_code": "string",
    "new_password": "string"
  }
  ```
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "message": "Password reset successful."
  }
  ```
- **Response (400 - Content-Type: application/json)**:
  ```json
  {
    "message": "Invalid verification code."
  }
  ```

#### 7. **Login**
- **URL**: `/v1/accounts/login/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "user_id": 1,
    "username": "example_user",
    "token": "abcdef123456"
  }
  ```
- **Response (400 - Content-Type: application/json)**:
  ```json
  {
    "message": "Invalid credentials."
  }
  ```

#### 8. **Logout**
- **URL**: `/v1/accounts/logout/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "refresh": "string"
  }
  ```
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "detail": "Successfully logged out."
  }
  ```
- **Response (400 - Content-Type: application/json)**:
  ```json
  {
    "message": "Invalid refresh token."
  }
  ```

#### 9. **Register**
- **URL**: `/v1/accounts/register/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "email": "user@example.com",
    "verification_code": "string",
    "first_name": "string",
    "last_name": "string",
    "password": "string"
  }
  ```
- **Response (201 - Content-Type: application/json)**:
  ```json
  {
    "message": "Registration successful."
  }
  ```
- **Response (400 - Content-Type: application/json)**:
  ```json
  {
    "message": "Registration failed. Please try again."
  }
  ```

#### 10. **Send Verification Code**
- **URL**: `/v1/accounts/send-verification-code/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "email": "user@example.com"
  }
  ```
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "message": "Verification code sent."
  }
  ```
- **Response (400 - Content-Type: application/json)**:
  ```json
  {
    "message": "Invalid email address."
  }
  ```

---

### **Book and Review Endpoints 📚:**

#### 11. **Get Books**
- **URL**: `/v1/books/`
- **Method**: GET
- **Response (200 - Content-Type: application/json)**:
  ```json
  [
    {
      "id": 0,
      "title": "string",
      "isbn": "string",
      "description": "string",
      "published_date": "2019-08-24",
      "slug": "string",
      "condition": "new",
      "book_format": "physical",
      "page_count": 2147483647,
      "edition": "string",
      "publisher": "string",
      "language": "string",
      "shelf_location": "string",
      "image": "http://example.com",
      "digital_file": "http://example.com",
      "tags": [],
      "allow_rental": true,
      "available": true,
      "book_count": 2147483647,
      "available_count": 2147483647,
      "added_date": "2019-08-24T14:15:22Z",
      "author": 0,
      "category": 0
    }
  ]
  ```

#### 12. **Get Book Details**
- **URL**: `/v1/books/{identifier}/detail/`
- **Method**: GET
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "id": 0,
    "title": "string",
    "isbn": "string",
    "description": "string",
    "published_date": "2019-08-24",
    "slug": "string",
    "condition": "new",
    "book_format": "physical",
    "page_count": 2147483647,
    "edition": "string",
    "publisher": "string",
    "language": "string",
    "shelf_location": "string",
    "image": "http://example.com",
    "digital_file": "http://example.com",
    "tags": ["string"],
    "allow_rental": true,
    "available": true,
    "book_count": 2147483647,
    "available_count": 2147483647,
    "added_date": "2019-08-24T14:15:22Z",
    "author": 0,
    "category": 0
  }
  ```

#### 13. **Get Reviews for a Book**
- **URL**: `/v1/books/{book_id}/reviews/`
- **Method**: GET
- **Response (200 - Content-Type: application/json)**:
  ```json
  [
    {
      "id": 0,
      "book": 0,
      "book_title": "string",
      "user": 0,
      "user_username": "string",
      "rating": 1,
      "review": "string",
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
  ```

#### 14. **Add a Review for a Book**
- **URL**: `/v1/books/{book_id}/reviews/`
- **Method**: POST
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "rating": 0,
    "review": "string"
  }
  ```
- **Response (201 - Content-Type: application/json)**:
  ```json
  {
    "id": 0,
    "book": 0,
    "book_title": "string",
    "user": 0,
    "user_username": "string",
    "rating": 1,
    "review": "string",
    "created_at": "2019-08-24T14:15:22Z"
  }
  ```

#### 15. **Update a Review**
- **URL**: `/v1/reviews/{review_id}/`
- **Method**: PUT
- **Request Payload (Content-Type: application/json)**:
  ```json
  {
    "rating": 1,
    "review": "string"
  }
  ```
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "id": 0,
    "book": 0,
    "book_title": "string",
    "user": 0,
    "user_username": "string",
    "rating": 1,
    "review": "string",
    "created_at": "2019-08-24T14:15:22Z"
  }
  ```

#### 16. **Delete a Review**
- **URL**: `/v1/reviews/{review_id}/`
- **Method**: DELETE
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "message": "Review deleted successfully."
  }
  ```

---

### **Category Endpoints 📂:**

#### 17. **Get Categories**
- **URL**: `/v1/categories/`
- **Method**: GET
- **Response (200 - Content-Type: application/json)**:
  ```json
  [
    {
      "id": 0,
      "name": "string",
      "slug": "string",
      "icon": "http://example.com",
      "order": -2147483648,
      "is_active": true,
      "super_category": 0,
      "super_category_name": "string"
    }
  ]
  ```

#### 18. **Get Category Details**
- **URL**: `/v1/categories/{identifier}/detail/`
- **Method**: GET
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "id": 0,
    "name": "string",
    "slug": "string",
    "icon": "http://example.com",
    "order": -2147483648,
    "is_active": true,
    "super_category": 0,
    "super_category_name": "string"
  }
  ```

#### 19. **Get Subcategory Details**
- **URL**: `/v1/subcategories/{identifier}/detail/`
- **Method**: GET
- **Response (200 - Content-Type: application/json)**:
  ```json
  {
    "id": 0,
    "name": "string",
    "slug": "string",
    "icon": "http://example.com",
    "order": -2147483648,
    "is_active": true,
    "super_category": 0
  }
  ```

---

### GET /v1/events/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "start_time": "2019-08-24T14:15:22Z",
    "end_time": "2019-08-24T14:15:22Z",
    "location": "string",
    "image": "http://example.com",
    "video": "http://example.com"
  }
]
```

---

### GET /v1/events/{event_id}/
**Response samples (200, 404)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "start_time": "2019-08-24T14:15:22Z",
  "end_time": "2019-08-24T14:15:22Z",
  "location": "string",
  "image": "http://example.com",
  "video": "http://example.com"
}
```

---

### GET /v1/overdue_fines/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 0,
    "rental_id": 0,
    "book_title": "string",
    "user_email": "user@example.com",
    "overdue_days": 2147483647,
    "fine_amount": "string"
  }
]
```

---

### GET /v1/overdue_fines/{id}/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "rental_id": 0,
  "book_title": "string",
  "user_email": "user@example.com",
  "overdue_days": 2147483647,
  "fine_amount": "string"
}
```

---

### GET /v1/payments/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 1,
    "amount": 100,
    "status": "Completed",
    "payment_date": "2024-03-30T12:00:00Z"
  },
  {
    "id": 2,
    "amount": 50,
    "status": "Pending",
    "payment_date": "2024-03-30T14:00:00Z"
  }
]
```

---

### POST /v1/payments/
**Request samples**
- **Payload** (Content type: `application/json`)

```json
{
  "book": 0,
  "amount": "string",
  "payment_method": "card"
}
```

**Response samples (201)**
- **Content type**: `application/json`

```json
{
  "id": 3,
  "amount": 200,
  "status": "Pending",
  "payment_date": "2024-03-30T15:00:00Z"
}
```

---

### GET /v1/payments/{payment_id}/detail/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "id": 1,
  "amount": 100,
  "status": "Completed",
  "payment_date": "2024-03-30T12:00:00Z"
}
```

---

### DELETE /v1/payments/{payment_id}/detail/
---

### GET /v1/preferences/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "theme": "dark",
  "notifications_enabled": true,
  "language": "en"
}
```

---

### GET /v1/preferences/{id}/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "theme": "light",
  "notifications_enabled": false,
  "language": "fr"
}
```

---

### GET /v1/purchase-history/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 0,
    "user_id": 0,
    "user_name": "string",
    "book_id": 0,
    "book_title": "string",
    "purchase_date": "2019-08-24",
    "sale_price": "string"
  }
]
```

---

### GET /v1/purchase-history/{id}/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "user_id": 0,
  "user_name": "string",
  "book_id": 0,
  "book_title": "string",
  "purchase_date": "2019-08-24",
  "sale_price": "string"
}
```

---

### DELETE /v1/purchase-history/{id}/
---

### GET /v1/recommendations/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 1,
    "book_title": "Book Title 1",
    "author": "Author 1",
    "recommendation_date": "2025-03-30",
    "rating": 4.5
  },
  {
    "id": 2,
    "book_title": "Book Title 2",
    "author": "Author 2",
    "recommendation_date": "2025-03-29",
    "rating": 5
  }
]
```

---

### GET /v1/recommendations/{id}/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "id": 1,
  "book_title": "Book Title 1",
  "author": "Author 1",
  "recommendation_date": "2025-03-30",
  "rating": 4.5
}
```

---

### GET /v1/rental-history/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 0,
    "user": "string",
    "book": "string",
    "rental_start_date": "2019-08-24",
    "rental_end_date": "2019-08-24",
    "rental_duration": "3_days",
    "rental_price": "string"
  }
]
```

---

### GET /v1/rental-history/{id}/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "user": "string",
  "book": "string",
  "rental_start_date": "2019-08-24",
  "rental_end_date": "2019-08-24",
  "rental_duration": "3_days",
  "rental_price": "string"
}
```

---

### DELETE /v1/rental-history/{id}/
---

### GET /v1/rental-prices/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 0,
    "book": 0,
    "book_title": "string",
    "duration": {},
    "duration_display": "string",
    "price_3_days": "string",
    "price_1_week": "string",
    "price_1_month": "string"
  }
]
```

---

### GET /v1/rental-prices/{id}/detail/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "book": 0,
  "book_title": "string",
  "duration": {},
  "duration_display": "string",
  "price_3_days": "string",
  "price_1_week": "string",
  "price_1_month": "string"
}
```

---

### GET /v1/rental-schedules/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 0,
    "user": 0,
    "book": 0,
    "rental_duration": "3_days",
    "rental_price": "string"
  }
]
```

---

### POST /v1/rental-schedules/
**Request samples**
- **Payload** (Content type: `application/json`)

```json
{
  "user": 0,
  "book": 0,
  "rental_duration": "3_days",
  "rental_price": "string"
}
```

**Response samples (201)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "user": 0,
  "book": 0,
  "rental_duration": "3_days",
  "rental_price": "string"
}
```

---

### GET /v1/rental-schedules/{id}/detail/
**Response samples (200)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "user": 0,
  "book": 0,
  "rental_duration": "3_days",
  "rental_price": "string"
}
```

---

### DELETE /v1/rental-schedules/{id}/detail/
---

### GET /v1/sale-transactions/
**Response samples (200, 403, 404)**
- **Content type**: `application/json`

```json
[
  {
    "id": 0,
    "user": "string",
    "book": "string",
    "sale_price": "string",
    "sale_date": "2019-08-24",
    "status": "pending"
  }
]
```

---

### GET /v1/sale-transactions/{id}/
**Response samples (200, 403, 404)**
- **Content type**: `application/json`

```json
{
  "id": 0,
  "user": "string",
  "book": "string",
  "sale_price": "string",
  "sale_date": "2019-08-24",
  "status": "pending"
}
```

---

### GET /v1/sale_price/
**Response samples (200)**
- **Content type**: `application/json`

```json
[
  {
    "id": 1,
    "price": "100.00",
    "currency": "USD"
  },
  {
    "id": 2,
    "price": "150.00",
    "currency": "EUR"
  }
]
```

---

### GET /v1/sale_price/{id}/
**Response samples (200, 404)**
- **Content type**: `application/json`

```json
{
  "id": 1,
  "price": "100.00",
  "currency": "USD"
}
```