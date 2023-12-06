using var sr = new StreamReader("input.txt");
var input = sr.ReadToEnd();

var sections = input.Split("\r\n\r\n");

var almanac = new Almanac(
    ParseSeeds(sections[0]),
    ParseMap(sections[1]),
    ParseMap(sections[2]),
    ParseMap(sections[3]),
    ParseMap(sections[4]),
    ParseMap(sections[5]),
    ParseMap(sections[6]),
    ParseMap(sections[7])
);

PrintLn($"{almanac.GetLowestSeedLocation()}");

return 0;

// Util below

IEnumerable<long> ParseSeeds(string seedsInput)
{
    var seeds = seedsInput.Split(": ").Last().Split(" ").Select(long.Parse).ToArray();
    for (int i = 0; i < seeds.Length - 1; i += 2)
    {
        var start = seeds[i];
        var length = seeds[i + 1];
        PrintLn($"Starting pair {start} {length}");
        for (int j = 0; j < length; j++)
        {
            if (j % 10000000 == 0)
            {
                Print(".");
            }
            yield return start + j;
        }
        PrintLn($"Finished pair {start} {length}");
    }
}

AlmanacMap ParseMap(string section)
{
    var lines = section.Split(":")[1].Split("\r\n").Where(l => !string.IsNullOrWhiteSpace(l));
    return new AlmanacMap(lines);
}

void Print(string txt) => Console.Write(txt);
void PrintLn(string txt) => Console.WriteLine(txt);

class Almanac
{
    private readonly IEnumerable<long> _seeds;
    private readonly AlmanacMap _seedToSoil;
    private readonly AlmanacMap _soilToFertilizer;
    private readonly AlmanacMap _fertilizerToWater;
    private readonly AlmanacMap _waterToLight;
    private readonly AlmanacMap _lightToTemperature;
    private readonly AlmanacMap _temperatureToHumidity;
    private readonly AlmanacMap _humidityToLocation;

    public Almanac(IEnumerable<long> seeds, AlmanacMap seedToSoil, AlmanacMap soilToFertilizer, AlmanacMap fertilizerToWater,
        AlmanacMap waterToLight, AlmanacMap lightToTemperature, AlmanacMap temperatureToHumidity,
        AlmanacMap humidityToLocation)
    {
        _seeds = seeds;
        _seedToSoil = seedToSoil;
        _soilToFertilizer = soilToFertilizer;
        _fertilizerToWater = fertilizerToWater;
        _waterToLight = waterToLight;
        _lightToTemperature = lightToTemperature;
        _temperatureToHumidity = temperatureToHumidity;
        _humidityToLocation = humidityToLocation;
    }

    public long GetLowestSeedLocation()
    {
        var locations = GetSeedLocations();
        return locations.Min();
    }

    private IEnumerable<long> GetSeedLocations()
    {
        var locations = new List<long>();
        foreach (var seed in _seeds)
        {
            var soil = _seedToSoil.GetMappedValue(seed);
            var fertilizer = _soilToFertilizer.GetMappedValue(soil);
            var water = _fertilizerToWater.GetMappedValue(fertilizer);
            var light = _waterToLight.GetMappedValue(water);
            var temperature = _lightToTemperature.GetMappedValue(light);
            var humidity = _temperatureToHumidity.GetMappedValue(temperature);
            var location = _humidityToLocation.GetMappedValue(humidity);

            locations.Add(location);
        }

        return locations;
    }
}

record AlmanacMapEntry(long DestinationRangeStart, long SourceRangeStart, long RangeLength);

class AlmanacMap
{
    private readonly List<AlmanacMapEntry> _entries = new();
    
    public AlmanacMap(IEnumerable<string> entries)
    {
        foreach (var entry in entries)
        {
            var numbers = entry.Split(" ").Select(long.Parse).ToArray();
            _entries.Add(new AlmanacMapEntry(numbers[0], numbers[1], numbers[2]));
        }
    }

    public long GetMappedValue(long source)
    {
        foreach (var entry in _entries)
        {
            if (entry.SourceRangeStart <= source && source <= entry.SourceRangeStart + entry.RangeLength)
            {
                return source + (entry.DestinationRangeStart - entry.SourceRangeStart);
            }
        }
        
        return source;
    }
}

