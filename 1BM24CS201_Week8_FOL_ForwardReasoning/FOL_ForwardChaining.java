
import java.util.*;

public class FOL_ForwardChaining {

    static Scanner sc = new Scanner(System.in);
    static Set<String> KB = new LinkedHashSet<>();

    // Add fact to Knowledge Base
    static boolean addFact(String fact) {
        if (KB.add(fact)) {
            System.out.println("New Fact Generated: " + fact);
            return true;
        }
        return false;
    }

    public static void main(String[] args) {

        System.out.println("================================");
        System.out.println(" FOL FORWARD CHAINING SYSTEM");
        System.out.println("================================");

        System.out.println("\nEnter FOL facts one by one.");
        System.out.println("Type DONE when finished.\n");

        // Manual user input
        while (true) {
            System.out.print("Enter fact: ");
            String fact = sc.nextLine().trim();

            if (fact.equalsIgnoreCase("DONE"))
                break;

            if (!fact.isEmpty()) {
                KB.add(fact);
            }
        }

        System.out.println("\nInitial Knowledge Base:");
        for (String fact : KB) {
            System.out.println(fact);
        }

        System.out.println("\nApplying Forward Chaining...\n");

        boolean changed;

        do {
            changed = false;

            // Rule 1: Missiles are weapons
            if (KB.contains("Missile(T1)")) {
                if (addFact("Weapon(T1)"))
                    changed = true;
            }

            // Rule 2: Robert sells missiles owned by A
            if (KB.contains("Missile(T1)") &&
                KB.contains("Owns(A,T1)")) {

                if (addFact("Sells(Robert,T1,A)"))
                    changed = true;
            }

            // Rule 3: Enemy of America is hostile
            if (KB.contains("Enemy(A,America)")) {
                if (addFact("Hostile(A)"))
                    changed = true;
            }

            // Rule 4: Crime rule
            if (KB.contains("American(Robert)") &&
                KB.contains("Weapon(T1)") &&
                KB.contains("Sells(Robert,T1,A)") &&
                KB.contains("Hostile(A)")) {

                if (addFact("Criminal(Robert)"))
                    changed = true;
            }

        } while (changed);

        System.out.println("\n================================");
        System.out.println("FINAL RESULT");
        System.out.println("================================");

        if (KB.contains("Criminal(Robert)")) {
            System.out.println("Robert is CRIMINAL.");
            System.out.println("Query Criminal(Robert) is PROVED.");
        } else {
            System.out.println("Robert is NOT PROVED CRIMINAL.");
            System.out.println("Query Criminal(Robert) is NOT PROVED.");
        }

        System.out.println("\nFinal Knowledge Base:");
        for (String fact : KB) {
            System.out.println(fact);
        }

        sc.close();
    }
}
