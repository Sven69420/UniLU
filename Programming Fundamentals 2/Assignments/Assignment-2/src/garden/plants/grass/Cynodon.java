package garden.plants.grass;

import java.util.Objects;

public class Cynodon extends Grass {
    public Cynodon() {
        super("Cynodon", 0.3);  // Name and water consumption specific to Cynodon
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Cynodon)) return false;
        return super.equals(obj);  // Leveraging Grass's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}
