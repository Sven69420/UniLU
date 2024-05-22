package garden.plants.grass;

import java.util.Objects;
import garden.plants.Plant;

public class Grass extends Plant {
    public Grass(String name, double waterConsumption) {
        super(name, waterConsumption);
    }

    @Override
    public String colour(int season) {
        return "Green"; // Grass is always green, regardless of season
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Grass other = (Grass) obj;
        return Objects.equals(name, other.name) &&
               waterConsumption == other.waterConsumption; // Compare waterConsumption if relevant
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, waterConsumption); // Include waterConsumption in hashCode calculation
    }
}
