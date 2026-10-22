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


/////////////Formatting
string name = " eeee ee e eee";
decimal price = 1234.5m;
Console.WriteLine($"£{price:N2}");                 // £1,234.50
Console.WriteLine($"{DateTime.Today:yyyy-MM-dd}"); // e.g. 2026-10-22
Console.WriteLine($"[{name,-10}]");                // left-align in 10 characters
Console.WriteLine($"[{name,10}]");                 // right-align in 10 characters


///MISC
a = "E";
b = "EE";

Console.WriteLine(name[1..3]); 
Console.WriteLine(name[^1]);
string.Equals(a, b, StringComparison.OrdinalIgnoreCase);
string.IsNullOrWhiteSpace(name);
