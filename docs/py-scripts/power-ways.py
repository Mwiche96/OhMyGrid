import requests
import json
import re
from datetime import datetime
import sys
import os

def convert_to_mw(value):
    """
    Converts a power capacity string (e.g., "100 MW", "500 kW", "1 GW") to megawatts.
    """
    if not value:
        return 0

    val_str = str(value).strip().lower()
    
    # Improved regex to handle various formats
    match = re.search(r'(\d+(\.\d+)?)\s*(gw|mw|kw)?', val_str)
    
    if not match:
        return 0

    num = float(match.group(1))
    unit = match.group(3)

    if unit == 'gw':
        return num * 1000
    if unit == 'kw':
        return num / 1000
    
    # Assume MW if no unit is specified
    return num

def fetch_and_process_power_data():
    """
    Fetches both power plant and substation data in a single Overpass API request and processes it.
    """
    print("🚀 Starting combined Overpass API request...")
    
    overpass_url = "https://overpass-api.de/api/interpreter" 
    
    # This query gets the full data for both plants and substations in one go
    query = """
    [out:json][timeout:900];
    (
      // Query for power plants
      nwr["power"="plant"](user_touched:"Andreas Hernandez","Tobias Augspurger","davidtt92","Mwiche","relaxxe");
      nwr["power"="plant"](user: "Russ","map-dynartio","overflorian","nlehuby","ben10dynartio","InfosReseaux")(newer:"2025-03-01T00:00:00Z");
      
      // Query for substations
      nwr["power"="substation"](user_touched:"Andreas Hernandez","Tobias Augspurger","davidtt92","Mwiche","relaxxe");
      nwr["power"="substation"](user: "Russ","map-dynartio","overflorian","nlehuby","ben10dynartio","InfosReseaux")(newer:"2025-03-01T00:00:00Z");
    );
    out body;
    >;
    out skel qt;
    """

    try:
        print("📡 Sending request to Overpass API. This may take several minutes...")
        # A 15-minute timeout for the entire request
        response = requests.post(overpass_url, data={"data": query}, timeout=920) 
        response.raise_for_status()
        data = response.json()
        print(f"✅ Received {len(data.get('elements', []))} total elements from API.")

        total_capacity_mw = 0
        plant_count = 0
        substation_count = 0

        # Process all elements in a single loop
        for element in data.get("elements", []):
            tags = element.get("tags", {})
            power_type = tags.get("power")

            if power_type == "plant":
                plant_count += 1
                if "plant:output:electricity" in tags:
                    capacity_str = tags["plant:output:electricity"]
                    capacity_mw = convert_to_mw(capacity_str)
                    total_capacity_mw += capacity_mw
            
            elif power_type == "substation":
                substation_count += 1
        
        print(f"📊 Processed {plant_count} plants with total capacity {total_capacity_mw:.2f} MW")
        print(f"📊 Processed {substation_count} substations")

        return {
            "total_capacity_mw": round(total_capacity_mw, 2),
            "plant_count": plant_count,
            "substation_count": substation_count,
            "updated": datetime.utcnow().isoformat() + "Z"
        }

    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: API request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Failed to decode JSON response: {e}")
        return None

if __name__ == "__main__":
    print("Script starting...")
    power_data = fetch_and_process_power_data()
    
    if power_data:
        os.makedirs("docs/data", exist_ok=True)
        file_path = "docs/data/power-stats.json"
        with open(file_path, "w") as f:
            json.dump(power_data, f, indent=2)
        print(f"\n✅ Successfully updated data to {file_path}")
    else:
        print("\n❌ CRITICAL: Failed to generate power data. Exiting with error.")
        sys.exit(1)