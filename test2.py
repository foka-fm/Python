element=(input("Что вы хотите разместить? "))
print(("Как называется элемент куда вы хотите разместить"), element+"?")
box=input()
print("сколько", element, "вмещается в 1", box)
elemetns_in_box=int(input())
print("сколько", element,"вы имеете?")
elements_have=int(input())
kol_ostatkov = elements_have % elemetns_in_box
kol_box=elements_have // elemetns_in_box
print("Вам потребуется",kol_box,"количества", box,"для", elements_have, element )
print("В остатке останется", kol_ostatkov, element )
