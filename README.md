# Choreography Kata

A kata to learn and practice Choreography as opposed to Orchestration, as in a microservices architecture

### Enoncé du problème


Considérons un système de distributions de billets de spectacles en ligne. Le processus de vente consiste typiquement à Réserver (Booking), puis à réduire l'inventaire en correspondance s'il reste suffisamment de place (Inventory), puis à envoyer les billets (Ticketing), chacune de ces étapes étant un service distinct.

*Pour rester simple, chaque service ne fera rien d'autre que prétendre avoir terminé son travail et assurer la coordination d'ensemble.*

Les étapes :

**Approche traditionnelle**

1. Créer chaque service au plus simple (au plus naïf) et les faire s'appeler entre eux pour implémenter le workflow complet. Proposer un refactoring pour simplifier Booking.
1. Extraire la partie orchestration hors du service Booking, dans un nouveau service. Reconnaitre le design pattern classique auquel il correspond.
1. L'acheteur n'est pas informé s'il n'y a plus de place, il faut ajouter une notification (SMS ou email) dans ce cas. Ajouter le nouveau service Notification et faire en sorte q'il soit appelé quand nécessaire.
1. Observer et commenter les changements nécessaires lors de l'ajout (ou la suppression) de nouveaux services. Proposer une approche alternative.

**Approche alternative**

1. Introduire votre propre EventBus sous forme d'un simple pattern Observer (exemple de code ci-après), et transformer les services pour que toute la coordination se passe au travers du bus, sans le service Notification dans un premier temps.
1. Ajouter le service Notification, puis observer et commenter les changements nécessaires lors de l'ajout (ou la suppression) de nouveaux services. 
1. Comparer les deux approches, observer comment la logique du workflow est fragmentée dans chaque service. En débrief, donner les avantages et inconvénients respectifs de chaque approche, et quelles contraintes sont nécessaires pour respecter le principe Open-Close.


```java
/** The listener interface */
public interface Listener {
  void onMessage(Object msg);
}

/**
 * A simple in-memory, observer-pattern-based single-threaded message bus for designing architecture and testing using unit tests before switching to using actual middleware
 */
public class MessageBus {
    private List<Listener> subs = new ArrayList<Listener>();

    public void subscribe(Listener l) {
        this.subs.add(l);
    }

    public void send(Object msg) { 
        for (Listener l : subs) {
            l.onMessage(msg);
        }
    }
}
```

Si vous le souhaitez, vous pouvez aussi n'envoyer que des messages de type événements métier :

```java
/**
 * A basic event with a name and one single integer value
 */
public class Event {
  private final String name;
  private final int value;

  public Event(String name, int value) {
    this.name = name;
    this.value = value;
  }

  public String getName() {return name;}
  public int getValue() {return value;}
}
```


Ce kata couvre les aspects **Event-Driven Architecture**, **Choreography over Orchestration** et **Smart Endpoints, Dump Pipes*, qui ensemble font le style d'architecture microservices.
