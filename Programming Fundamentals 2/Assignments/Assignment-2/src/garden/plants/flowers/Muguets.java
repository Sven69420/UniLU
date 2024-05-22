package garden.plants.flowers;

import java.util.Objects;
import garden.colours.*;

public class Muguets extends Flower {
    public Muguets() {
        super("Muguets", 0.3, null, Colours.WHITE, Colours.GREEN, "None"); // Initialize with the specific characteristics of Muguets
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Muguets)) return false;
        Muguets muguets = (Muguets) obj;
        return super.equals(muguets); // Leveraging the Flower's equals implementation if applicable
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}
