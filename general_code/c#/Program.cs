string names = "apple, banana ,cherry";
string[] pieces = names.Split(',', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
string collected = string.Join(" | ", pieces)