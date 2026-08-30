from stationeers_pytrapic.symbols import *

# LogicBatchMethod.Count returns the number of matching devices on the network.
# The logic type is still required by the instruction (and still validated in-game
# by CanLogicRead), but is ignored when computing the result. PrefabHash, NameHash
# and ReferenceId are the three types CanLogicRead accepts unconditionally, so one
# of those is the safe pairing. PrefabHash is shortest in compact output (84 vs 268
# and 217), which is the mode that matters when you are near the size limit.
n_lights = FlashingLights.PrefabHash.Count

# batch method after the logic type
n_batteries = Batteries.Charge.Count
# batch method before the logic type. Covered once, deliberately: if Devices.Count
# ever gains a bare shorthand (Batteries.Count meaning Batteries.PrefabHash.Count),
# this form is the one that would have to change. One case guards it without tying
# the rest of the test to it.
n_batteries2 = Batteries.Count.Charge
# named batch
n_named = Batteries["Main"].Charge.Count
# slot batch
n_slots = Autolathes.Export.Occupied.Count

# the other batch methods still resolve
avg = Batteries.Charge.Average
total = Batteries.Sum.Charge

db.Setting = n_lights + n_batteries + n_batteries2 + n_named + n_slots + avg + total
