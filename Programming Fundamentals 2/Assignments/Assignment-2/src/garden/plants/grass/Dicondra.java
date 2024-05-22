package garden.plants.grass;

import java.util.Objects;

public class Dicondra extends Grass {
    public Dicondra() {
        super("Dicondra", 0.1);  // Name and water consumption specific to Dicondra
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Dicondra)) return false;
        return super.equals(obj);  // Leveraging Grass's equals implementation
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode());
    }
}
