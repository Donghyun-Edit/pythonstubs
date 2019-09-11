from typing import Tuple, Set, Iterable, List


class GH_BackgroundStyle:
    Solid = 0
    Hatch = 1
    GradientLeftRight = 10
    GradientTopBottom = 11


class GH_BackgroundSettings:
    @property
    def Style(self) -> GH_BackgroundStyle: ...
    @Style.setter
    def Style(self, AutoPropertyValue: GH_BackgroundStyle) -> None: ...
    @property
    def Hatch(self) -> HatchStyle: ...
    @Hatch.setter
    def Hatch(self, AutoPropertyValue: HatchStyle) -> None: ...
    @property
    def Colour1(self) -> Color: ...
    @Colour1.setter
    def Colour1(self, AutoPropertyValue: Color) -> None: ...
    @property
    def Colour2(self) -> Color: ...
    @Colour2.setter
    def Colour2(self, AutoPropertyValue: Color) -> None: ...


class GH_PageSettings:
    @property
    def DrawPage(self) -> bool: ...
    @DrawPage.setter
    def DrawPage(self, AutoPropertyValue: bool) -> None: ...
    @property
    def DrawShadow(self) -> bool: ...
    @DrawShadow.setter
    def DrawShadow(self, AutoPropertyValue: bool) -> None: ...
    @property
    def DrawGrid(self) -> bool: ...
    @DrawGrid.setter
    def DrawGrid(self, AutoPropertyValue: bool) -> None: ...
    @property
    def EdgeColour(self) -> Color: ...
    @EdgeColour.setter
    def EdgeColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def FillColour(self) -> Color: ...
    @FillColour.setter
    def FillColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def ShadowColour(self) -> Color: ...
    @ShadowColour.setter
    def ShadowColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def ShadowSize(self) -> int: ...
    @ShadowSize.setter
    def ShadowSize(self, AutoPropertyValue: int) -> None: ...
    @property
    def GridColour(self) -> Color: ...
    @GridColour.setter
    def GridColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def GridWidth(self) -> int: ...
    @GridWidth.setter
    def GridWidth(self, AutoPropertyValue: int) -> None: ...
    @property
    def GridHeight(self) -> int: ...
    @GridHeight.setter
    def GridHeight(self, AutoPropertyValue: int) -> None: ...
    @property
    def GridPattern(self) -> Set(Single): ...
    @GridPattern.setter
    def GridPattern(self, AutoPropertyValue: Set(Single)) -> None: ...


class GH_WireSettings:
    @property
    def DefaultColour(self) -> Color: ...
    @DefaultColour.setter
    def DefaultColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def EmptyColour(self) -> Color: ...
    @EmptyColour.setter
    def EmptyColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def SelectedColour0(self) -> Color: ...
    @SelectedColour0.setter
    def SelectedColour0(self, AutoPropertyValue: Color) -> None: ...
    @property
    def SelectedColour1(self) -> Color: ...
    @SelectedColour1.setter
    def SelectedColour1(self, AutoPropertyValue: Color) -> None: ...


class GH_ObjectSettings:
    @property
    def GroupColour(self) -> Color: ...
    @GroupColour.setter
    def GroupColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def PanelColour(self) -> Color: ...
    @PanelColour.setter
    def PanelColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def ZuiFillColour(self) -> Color: ...
    @ZuiFillColour.setter
    def ZuiFillColour(self, AutoPropertyValue: Color) -> None: ...
    @property
    def ZuiEdgeColour(self) -> Color: ...
    @ZuiEdgeColour.setter
    def ZuiEdgeColour(self, AutoPropertyValue: Color) -> None: ...


class GH_PaletteSettings:
    @property
    def NormalStandard(self) -> GH_PaletteStyle: ...
    @NormalStandard.setter
    def NormalStandard(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def NormalSelected(self) -> GH_PaletteStyle: ...
    @NormalSelected.setter
    def NormalSelected(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def HiddenStandard(self) -> GH_PaletteStyle: ...
    @HiddenStandard.setter
    def HiddenStandard(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def HiddenSelected(self) -> GH_PaletteStyle: ...
    @HiddenSelected.setter
    def HiddenSelected(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def LockedStandard(self) -> GH_PaletteStyle: ...
    @LockedStandard.setter
    def LockedStandard(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def LockedSelected(self) -> GH_PaletteStyle: ...
    @LockedSelected.setter
    def LockedSelected(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def WarningStandard(self) -> GH_PaletteStyle: ...
    @WarningStandard.setter
    def WarningStandard(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def WarningSelected(self) -> GH_PaletteStyle: ...
    @WarningSelected.setter
    def WarningSelected(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def ErrorStandard(self) -> GH_PaletteStyle: ...
    @ErrorStandard.setter
    def ErrorStandard(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...
    @property
    def ErrorSelected(self) -> GH_PaletteStyle: ...
    @ErrorSelected.setter
    def ErrorSelected(self, AutoPropertyValue: GH_PaletteStyle) -> None: ...


class GH_Theme:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, other: GH_Theme): ...
    @property
    def DefaultTheme() -> GH_Theme: ...
    @property
    def BackGround(self) -> GH_BackgroundSettings: ...
    @property
    def Page(self) -> GH_PageSettings: ...
    @property
    def Wires(self) -> GH_WireSettings: ...
    @property
    def Objects(self) -> GH_ObjectSettings: ...
    @property
    def Palettes(self) -> GH_PaletteSettings: ...
    def LoadTheme(self) -> None: ...
    def SaveTheme(self) -> None: ...
    def Write(self, writer: GH_IWriter) -> bool: ...
    def Read(self, reader: GH_IReader) -> bool: ...