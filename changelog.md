v0.3.0
- Several changes to @Property for read-only
- Direct lookup on attribute.value from items. Allows such code as
```
t=myitem.Time
v=myItem.Value
otheritem.Value = 2*v
```
- Added some example modules
- Direct access to VQS from Hive
- Added some more attributes such as item_id
- Limiting exported symbols (all)
- Changed `type` to `module_type` to avoid conflicts with the resulved `type`
- Added module.add_item
- Added the possibility to write item-attr
- Item-attr understands enumerated values and returns the correct value.
- Some of the common features are moved to a separate util module. This will be nice when we introduce a honeystore module.
- Time conversion utilities .net DateTime <=> python datetime
- Quality class to deal with OPC-quality

v0.2.0
- Created the initial module from previous work by LH and DKG (AL)