package garden.plants.flowers;

import java.util.Objects;
import garden.colours.Colours;

public class Rose extends Flower {
    public Rose(String color) {
        super("Rose", 0.4, Colours.BROWN, color, color, Colours.BROWN); // Initialize with the specific characteristics of a Rose
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Rose)) return false;
        Rose rose = (Rose) obj;
        return super.equals(rose); // Leveraging the Flower's equals implementation if applicable
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}
