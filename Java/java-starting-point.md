
BookingService,  InventoryService & TicketingService classes
```
public record BookingService() {

    public void book(int numberOfSeats) {
        // validate booking etc.
        System.out.println("BookingRequested");
    }
}

public class InventoryService {
    private int capacity;
    public InventoryService(int capacity) {
        this.capacity = capacity;
    }

    public int capacity() {
        return capacity;
    }

    public boolean reserveInventory(int numberOfSeats) {
        if (numberOfSeats <= capacity){
            capacity -= numberOfSeats;
            System.out.println("CapacityReserved "+ numberOfSeats);
            return true;
        }
        System.out.println("CapacityExceeded "+ numberOfSeats);
        return false;
    }
}


public record TicketingService() {
    public void printTickets(int numberOfSeats) {
        System.out.println("TicketPrinted: " + numberOfSeats);
    }
}
```
