### Aufgabe 1: Überlegen von API-Anfragen

1. **Produktsuche nach Keywords**  
   _"Als Nutzer möchte ich nach Produkten mit einem bestimmten Keyword suchen (z. B. ‘Laptop’)."_  
   **API-Request:**  
   ```
   GET /products?search=Laptop
   ```

2. **Filterung nach Preisspanne**  
   _"Als Nutzer möchte ich Produkte in einer bestimmten Preisspanne angezeigt bekommen (z. B. zwischen 20 und 100 Euro)."_  
   **API-Request:**  
   ```
   GET /products?minPrice=20&maxPrice=100
   ```

3. **Warenkorb anzeigen**  
   _"Als Nutzer möchte ich meine gespeicherten Artikel im Warenkorb anzeigen lassen."_  
   **API-Request:**  
   ```
   GET /cart
   ```

4. **Produktdetails ansehen**  
   _"Als Nutzer möchte ich die detaillierten Informationen zu einem Produkt einsehen (z. B. technische Details, Bewertungen)."_  
   **API-Request:**  
   ```
   GET /products/{productId}
   ```

5. **Produkt kaufen**  
   _"Als Nutzer möchte ich ein Produkt in meinem Warenkorb kaufen können."_  
   **API-Request:**
    ```
   POST /order
   Body: {
       "cartId": "12345",
       "paymentMethod": "CreditCard"
   }
   ```
