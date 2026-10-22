//////////////////////////////////STRING BUILDER
using System.Text;

var sb = new StringBuilder();

for(int i = 0; i < 3; i++){
    sb.Append($"NEW LINE").AppendLine();
}

string builtSB = sb.ToString();
Console.WriteLine(builtSB);



var sb2 = new StringBuilder();
for(int xx = 0; xx < 3; xx++){
    sb2.Append("E").AppendLine();
}
string newString = sb2.ToString();


//////////////////////////////////SPLIT JOIN
string names = "apple, banana ,cherry";
string[] pieces = names.Split(',', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
string collected = string.Join(" | ", pieces);
Console.WriteLine(collected);

if(collected.StartsWith("E")){
    
}

