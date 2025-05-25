# import spacy
# from spacy.tokens import DocBin

# # Sample training data: list of tuples (text, {"entities": [(start, end, label), ...]})
# TRAIN_DATA = [
#     ("Configure DUT with User Side VSI with VLAN 100 on Line1", {"entities": [(23, 39, "USER_VSI"), (45, 48, "VLAN"), (52, 57, "LINE")]}),
#     ("Set Forwarder to N:1 on Line2", {"entities": [(12, 15, "FORWARDER"), (19, 24, "LINE")]}),
#     # Add more examples here
# ]

# def main():
#     nlp = spacy.blank("en")  # create blank English model
#     db = DocBin()  # create DocBin object to store examples

#     for text, annotations in TRAIN_DATA:
#         doc = nlp.make_doc(text)
#         ents = []
#         for start, end, label in annotations.get("entities"):
#             span = doc.char_span(start, end, label=label)
#             if span is None:
#                 print(f"Skipping entity in: {text}")
#             else:
#                 ents.append(span)
#         doc.ents = ents
#         db.add(doc)

#     db.to_disk("backend/data/training_data.spacy")  # save training data

# if __name__ == "__main__":
#     main()
import spacy
from spacy.tokens import DocBin
import random

# Comprehensive training data based on the network testing example
TRAIN_DATA = [
    # Original test procedure examples
    ("Configure DUT with User Side VSI with VLAN 100 on Line1", {
        "entities": [(40, 48, "VLAN"), (49, 52, "VLAN_ID"), (56, 61, "LINE")]
    }),
    
    ("Configure DUT with Network Side VSI with VLAN 200 on Uplink1", {
        "entities": [(46, 54, "VLAN"), (55, 58, "VLAN_ID"), (62, 70, "UPLINK")]
    }),
    
    ("Send Upstream Traffic with VLAN100 and PBIT 5", {
        "entities": [(5, 13, "DIRECTION"), (27, 34, "VLAN"), (39, 44, "PBIT"), (45, 46, "PBIT_VALUE")]
    }),
    
    ("Send Downstream Traffic with VLAN200 and PBIT 7", {
        "entities": [(5, 15, "DIRECTION"), (29, 36, "VLAN"), (41, 46, "PBIT"), (47, 48, "PBIT_VALUE")]
    }),
    
    ("Ensure User Traffic is received without loss", {
        "entities": [(7, 11, "TRAFFIC_TYPE"), (21, 29, "ACTION")]
    }),
    
    ("Ensure Network Traffic is received without loss", {
        "entities": [(7, 14, "TRAFFIC_TYPE"), (24, 32, "ACTION")]
    }),
    
    # MAC Address examples
    ("Set Dst MAC to 99:02:03:04:05:06", {
        "entities": [(4, 7, "MAC_TYPE"), (11, 28, "MAC_ADDRESS")]
    }),
    
    ("Configure Src MAC as 98:0A:0B:0C:0D:0E", {
        "entities": [(10, 13, "MAC_TYPE"), (21, 38, "MAC_ADDRESS")]
    }),
    
    # Packet configuration examples
    ("Set NumPackets To Receive = 100", {
        "entities": [(4, 14, "PACKET_PARAM"), (28, 31, "PACKET_COUNT")]
    }),
    
    ("Configure NumPackets To Generate = 100", {
        "entities": [(10, 20, "PACKET_PARAM"), (35, 38, "PACKET_COUNT")]
    }),
    
    ("Add Packet L2 Header", {
        "entities": [(4, 10, "PACKET_COMPONENT"), (11, 13, "LAYER")]
    }),
    
    # VLAN and PBIT combinations
    ("VLAN = 100, PBIT = 5", {
        "entities": [(0, 4, "VLAN"), (7, 10, "VLAN_ID"), (12, 16, "PBIT"), (19, 20, "PBIT_VALUE")]
    }),
    
    ("VLAN = 200, PBIT = 7", {
        "entities": [(0, 4, "VLAN"), (7, 10, "VLAN_ID"), (12, 16, "PBIT"), (19, 20, "PBIT_VALUE")]
    }),
    
    # Entity and Equipment examples
    ("Entity2 = User Side Traffic Eqpt", {
        "entities": [(0, 7, "ENTITY"), (10, 14, "TRAFFIC_SIDE"), (20, 27, "EQUIPMENT_TYPE")]
    }),
    
    ("Entity3 = N/W Side Traffic Eqpt", {
        "entities": [(0, 7, "ENTITY"), (10, 13, "TRAFFIC_SIDE"), (19, 26, "EQUIPMENT_TYPE")]
    }),
    
    ("Configure DUT with Line2 interface", {
        "entities": [(10, 13, "DEVICE"), (19, 24, "LINE"), (25, 34, "COMPONENT")]
    }),
    
    ("Set up DUT on Line3 port", {
        "entities": [(7, 10, "DEVICE"), (14, 19, "LINE"), (20, 24, "COMPONENT")]
    }),
    
    # Traffic direction and types
    ("Generate upstream traffic on VLAN 150", {
        "entities": [(9, 17, "DIRECTION"), (29, 33, "VLAN"), (34, 37, "VLAN_ID")]
    }),
    
    ("Send downstream packets with VLAN 250", {
        "entities": [(5, 15, "DIRECTION"), (29, 33, "VLAN"), (34, 37, "VLAN_ID")]
    }),
    
    ("Transmit bidirectional traffic", {
        "entities": [(9, 22, "DIRECTION")]
    }),
    
    # Test verification examples
    ("Verify traffic is received without packet loss", {
        "entities": [(0, 6, "ACTION"), (7, 14, "TRAFFIC_TYPE"), (18, 26, "VERIFICATION"), (35, 46, "CONDITION")]
    }),
    
    ("Check that User Traffic flows correctly", {
        "entities": [(0, 5, "ACTION"), (11, 15, "TRAFFIC_TYPE")]
    }),
    
    ("Validate Network Traffic transmission", {
        "entities": [(0, 8, "ACTION"), (9, 16, "TRAFFIC_TYPE")]
    }),
    
    # Equipment and interface examples
    ("Connect to Uplink2 interface", {
        "entities": [(11, 18, "UPLINK"), (19, 28, "COMPONENT")]
    }),
    
    ("Attach DUT to Line4 connection", {
        "entities": [(7, 10, "DEVICE"), (14, 19, "LINE")]
    }),
    
    ("Configure User Side VSI parameters", {
        "entities": [(10, 14, "TRAFFIC_SIDE"), (20, 23, "VSI")]
    }),
    
    ("Set Network Side VSI configuration", {
        "entities": [(4, 11, "TRAFFIC_SIDE"), (17, 20, "VSI")]
    }),
    
    # Advanced VLAN configurations
    ("Create VLAN 300 tagged traffic", {
        "entities": [(7, 11, "VLAN"), (12, 15, "VLAN_ID"), (16, 22, "VLAN_TYPE")]
    }),
    
    ("Send untagged traffic on VLAN 400", {
        "entities": [(5, 13, "VLAN_TYPE"), (26, 30, "VLAN"), (31, 34, "VLAN_ID")]
    }),
    
    # Priority and QoS examples
    ("Set traffic priority to PBIT 3", {
        "entities": [(4, 11, "TRAFFIC_PARAM"), (24, 28, "PBIT"), (29, 30, "PBIT_VALUE")]
    }),
    
    ("Configure QoS with PBIT 6", {
        "entities": [(10, 13, "QOS"), (19, 23, "PBIT"), (24, 25, "PBIT_VALUE")]
    }),
    
    # Port and connection examples
    ("Connect Line5 to upstream port", {
        "entities": [(8, 13, "LINE"), (17, 25, "DIRECTION"), (26, 30, "COMPONENT")]
    }),
    
    ("Attach Line6 to downstream interface", {
        "entities": [(7, 12, "LINE"), (16, 26, "DIRECTION"), (27, 36, "COMPONENT")]
    }),
    
    # Forwarder examples
    ("Set Forwarder to N:1 mode", {
        "entities": [(4, 13, "FORWARDER"), (17, 20, "FORWARDER_TYPE")]
    }),
    
    ("Configure 1:N forwarder", {
        "entities": [(10, 13, "FORWARDER_TYPE"), (14, 23, "FORWARDER")]
    }),
    
    # Test equipment examples
    ("Use Test Equipment for traffic generation", {
        "entities": [(4, 8, "EQUIPMENT_TYPE"), (23, 30, "TRAFFIC_PARAM")]
    }),
    
    ("Setup DUT as bridge device", {
        "entities": [(6, 9, "DEVICE"), (13, 19, "DEVICE_TYPE")]
    }),
    
    # Mixed scenarios
    ("Configure DUT with User VSI VLAN 500 on Line7 and send traffic with PBIT 2", {
        "entities": [(10, 13, "DEVICE"), (19, 23, "TRAFFIC_SIDE"), (24, 27, "VSI"), (28, 32, "VLAN"), (33, 36, "VLAN_ID"), (40, 45, "LINE"), (69, 73, "PBIT"), (74, 75, "PBIT_VALUE")]
    }),
    
    ("Test downstream traffic from Network VSI VLAN 600 to User equipment", {
        "entities": [(5, 15, "DIRECTION"), (29, 36, "TRAFFIC_SIDE"), (37, 40, "VSI"), (41, 45, "VLAN"), (46, 49, "VLAN_ID"), (53, 57, "TRAFFIC_TYPE")]
    }),
    
    # Verification and testing
    ("Verify no packet loss occurs during transmission", {
        "entities": [(0, 6, "ACTION"), (10, 16, "PACKET_PARAM"), (30, 42, "PROCESS")]
    }),
    
    ("Monitor traffic flow between Line8 and Uplink3", {
        "entities": [(0, 7, "ACTION"), (8, 15, "TRAFFIC_PARAM"), (29, 34, "LINE"), (39, 46, "UPLINK")]
    }),
]

def create_additional_variations():
    """Generate additional training examples with variations"""
    variations = []
    
    # VLAN variations
    vlan_ids = ["100", "200", "300", "400", "500", "600", "700", "800"]
    lines = ["Line1", "Line2", "Line3", "Line4", "Line5", "Line6", "Line7", "Line8"]
    pbit_values = ["0", "1", "2", "3", "4", "5", "6", "7"]
    
    for vlan_id in vlan_ids:
        for line in lines:
            text = f"Configure DUT with VLAN {vlan_id} on {line}"
            entities = [(19, 23, "VLAN"), (24, 24+len(vlan_id), "VLAN_ID"), (28+len(vlan_id), 28+len(vlan_id)+len(line), "LINE")]
            variations.append((text, {"entities": entities}))
    
    # PBIT variations
    for pbit in pbit_values:
        text = f"Send traffic with PBIT {pbit}"
        entities = [(18, 22, "PBIT"), (23, 23+len(pbit), "PBIT_VALUE")]
        variations.append((text, {"entities": entities}))
    
    return variations[:50]  # Limit to 50 additional examples

def main():
    """Generate the complete training dataset"""
    
    # Combine base training data with variations
    all_training_data = TRAIN_DATA + create_additional_variations()
    
    print(f"Creating training dataset with {len(all_training_data)} examples...")
    
    # Create spaCy blank model and DocBin
    nlp = spacy.blank("en")
    db = DocBin()
    
    # Process each training example
    for text, annotations in all_training_data:
        doc = nlp.make_doc(text)
        ents = []
        
        # Create entity spans
        for start, end, label in annotations.get("entities", []):
            span = doc.char_span(start, end, label=label)
            if span is None:
                print(f"Skipping entity [{start}:{end}] '{text[start:end]}' in: {text}")
            else:
                ents.append(span)
        
        # Set entities and add to DocBin
        doc.ents = ents
        db.add(doc)
    
    # Save training data
    output_path = "backend/data/training_data.spacy"
    db.to_disk(output_path)
    print(f"Training data saved to: {output_path}")
    
    # Print summary of entity types
    entity_types = set()
    for _, annotations in all_training_data:
        for _, _, label in annotations.get("entities", []):
            entity_types.add(label)
    
    print(f"\nEntity types in training data: {sorted(entity_types)}")
    print(f"Total examples: {len(all_training_data)}")

if __name__ == "__main__":
    main()