export const getImage = async (type: "next" | "previous") => {
  const response = await fetch(`"http://127.0.0.1:5000/image?type=" + ${type}`);
  return await response.json();
};

export const getDefaultImage = async () => {
  return await JSON.parse(`{
    "image": "bin",
    "body": [
      {
        "defect_type":"hematome",
        "message":"Гематома",
        "color": "yellow"

      }
    ],
    "left_leg": [],
    "right_leg": [
      {
        "defect_type":"leg_not_fixed",
        "message":"нога не зафиксирована",
        "color": "yellow"
      },
      {
        "defect_type":"hematome",
        "message":"Гематома",
        "color": "yellow"

      }
    ],
    "left_wing": [{
        "defect_type":"open_break",
        "message":"открытый перелом",
        "color": "red"
      }],
    "right_wing": [{
        "defect_type":"closed_break",
        "message":"закрытый перелом",
        "color":"yellow"
      }],
    "decision": "PDS In"  
}`);
};
