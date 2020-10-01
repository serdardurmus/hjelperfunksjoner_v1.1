// Change The Colors! 

const colors = [{
    name: "Red",
    motto: "Rose Red",
  },
  {
    name: "Blue",
    motto: "Ocean Blue",
  },
  {
    name: "Gray",
    motto: "Smoke Gray",
  },
  {
    name: "Green",
    motto: "Grass Green",
  },
  {
    name: "Purple",
    motto: "Deep Purple",
  },
];

const color_list = ["AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGrey", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue", "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray", "Grey", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue", "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen", "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgrey", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "grey", "green", "greenyellow", "honeydew", "hotpink", "ındianred", "ındigo", "ıvory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgrey", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "rebeccapurple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen", "ALİCEBLUE", "ANTİQUEWHİTE", "AQUA", "AQUAMARİNE", "AZURE", "BEİGE", "BİSQUE", "BLACK", "BLANCHEDALMOND", "BLUE", "BLUEVİOLET", "BROWN", "BURLYWOOD", "CADETBLUE", "CHARTREUSE", "CHOCOLATE", "CORAL", "CORNFLOWERBLUE", "CORNSİLK", "CRİMSON", "CYAN", "DARKBLUE", "DARKCYAN", "DARKGOLDENROD", "DARKGRAY", "DARKGREY", "DARKGREEN", "DARKKHAKİ", "DARKMAGENTA", "DARKOLİVEGREEN", "DARKORANGE", "DARKORCHİD", "DARKRED", "DARKSALMON", "DARKSEAGREEN", "DARKSLATEBLUE", "DARKSLATEGRAY", "DARKSLATEGREY", "DARKTURQUOİSE", "DARKVİOLET", "DEEPPİNK", "DEEPSKYBLUE", "DİMGRAY", "DİMGREY", "DODGERBLUE", "FİREBRİCK", "FLORALWHİTE", "FORESTGREEN", "FUCHSİA", "GAİNSBORO", "GHOSTWHİTE", "GOLD", "GOLDENROD", "GRAY", "GREY", "GREEN", "GREENYELLOW", "HONEYDEW", "HOTPİNK", "INDİANRED", "INDİGO", "IVORY", "KHAKİ", "LAVENDER", "LAVENDERBLUSH", "LAWNGREEN", "LEMONCHİFFON", "LİGHTBLUE", "LİGHTCORAL", "LİGHTCYAN", "LİGHTGOLDENRODYELLOW", "LİGHTGRAY", "LİGHTGREY", "LİGHTGREEN", "LİGHTPİNK", "LİGHTSALMON", "LİGHTSEAGREEN", "LİGHTSKYBLUE", "LİGHTSLATEGRAY", "LİGHTSLATEGREY", "LİGHTSTEELBLUE", "LİGHTYELLOW", "LİME", "LİMEGREEN", "LİNEN", "MAGENTA", "MAROON", "MEDİUMAQUAMARİNE", "MEDİUMBLUE", "MEDİUMORCHİD", "MEDİUMPURPLE", "MEDİUMSEAGREEN", "MEDİUMSLATEBLUE", "MEDİUMSPRİNGGREEN", "MEDİUMTURQUOİSE", "MEDİUMVİOLETRED", "MİDNİGHTBLUE", "MİNTCREAM", "MİSTYROSE", "MOCCASİN", "NAVAJOWHİTE", "NAVY", "OLDLACE", "OLİVE", "OLİVEDRAB", "ORANGE", "ORANGERED", "ORCHİD", "PALEGOLDENROD", "PALEGREEN", "PALETURQUOİSE", "PALEVİOLETRED", "PAPAYAWHİP", "PEACHPUFF", "PERU", "PİNK", "PLUM", "POWDERBLUE", "PURPLE", "REBECCAPURPLE", "RED", "ROSYBROWN", "ROYALBLUE", "SADDLEBROWN", "SALMON", "SANDYBROWN", "SEAGREEN", "SEASHELL", "SİENNA", "SİLVER", "SKYBLUE", "SLATEBLUE", "SLATEGRAY", "SLATEGREY", "SNOW", "SPRİNGGREEN", "STEELBLUE", "TAN", "TEAL", "THİSTLE", "TOMATO", "TURQUOİSE", "VİOLET", "WHEAT", "WHİTE", "WHİTESMOKE", "YELLOW", "YELLOWGREEN"
]

const randomColorButton  = document.querySelector("#randomColorButton");
const addColorButton = document.querySelector("#setColorButton")
randomColorButton.addEventListener("click", changeColors);
addColorButton.addEventListener("click", setColors);

function changeColors() {
  const randomNumber = Math.floor(Math.random() * colors.length);
  document.querySelector("body").style.backgroundColor = colors[randomNumber].name;
  document.querySelector("#colorName").innerHTML = colors[randomNumber].name;
  document.querySelector("#colorDesc").innerHTML = colors[randomNumber].motto;
  console.log(colors);
}

function setColors () {
  const colorUserElements = document.querySelector(".colorInput");
  const colorData = colorUserElements.value.split(" ");
  if (colorData[1] == undefined) {alert("Renk ya da Motto eksik.");}
  else if (color_list.findIndex((color) => color === colorData[0]) !== -1) {
    if (colors.findIndex((color) => color === colorData[0]) !== -1) {
      colors.push(colorData);
      console.log(colors);
    } else {
    document.querySelector("body").style.backgroundColor = colorData[0];
    document.querySelector("#colorName").innerHTML = colorData[0];
    document.querySelector("#colorDesc").innerHTML = colorData[1];
    console.log(colors);}
  }

}




// Kullanıcı boş bir değer girerse?
// Kullanıcı geçersiz bir değer girerse?

// Bir input daha ekleyin: kullanıcıdan hex'a değer #eceff1?