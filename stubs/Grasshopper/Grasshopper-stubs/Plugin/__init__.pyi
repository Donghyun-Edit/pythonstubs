from typing import Tuple, Set, Iterable, List


class GH_ResourceGate:
    @property
    def WhiteIcon() -> Bitmap: ...
    @property
    def BlackIcon() -> Bitmap: ...
    @property
    def OK_40x40() -> Bitmap: ...
    @property
    def OK_24x24() -> Bitmap: ...
    @property
    def OK_16x16() -> Bitmap: ...
    @property
    def OK_12x12() -> Bitmap: ...
    @property
    def Warning_40x40() -> Bitmap: ...
    @property
    def Warning_24x24() -> Bitmap: ...
    @property
    def Warning_16x16() -> Bitmap: ...
    @property
    def Warning_12x12() -> Bitmap: ...
    @property
    def Error_40x40() -> Bitmap: ...
    @property
    def Error_24x24() -> Bitmap: ...
    @property
    def Error_16x16() -> Bitmap: ...
    @property
    def Error_12x12() -> Bitmap: ...
    @property
    def Info_40x40() -> Bitmap: ...
    @property
    def Info_24x24() -> Bitmap: ...
    @property
    def Info_16x16() -> Bitmap: ...
    @property
    def Info_12x12() -> Bitmap: ...


class GH_PluginUtil:
    def LoadGrasshopper(message: str) -> Tuple[bool, str]: ...
    def UnloadGrasshopper() -> bool: ...
    def SaveSettings() -> None: ...
    def SetFocus(hWnd: IntPtr) -> None: ...
    def BringWindowToTop(hWnd: IntPtr) -> bool: ...
    def SendMessage(hWnd: IntPtr, msg: int, wParam: int, lParam: IntPtr) -> IntPtr: ...
    def FocusOnRhino() -> None: ...
    def BringRhinoToTop() -> None: ...
    @overload
    def SendKeyCodeToRhino(key: int) -> None: ...
    @overload
    def SendKeyCodeToRhino(key: Char) -> None: ...
    @overload
    def SendKeyCodeToRhino(key: str) -> None: ...


class Commands:
    def Run_Grasshopper() -> bool: ...
    def Run_GrasshopperScripted() -> bool: ...
    @overload
    def Run_GrasshopperOpen() -> bool: ...
    @overload
    def Run_GrasshopperOpen(path: str) -> bool: ...
    def Run_GrasshopperDeveloperSettings() -> bool: ...
    def Run_GrasshopperUnloadPlugin() -> bool: ...
    def Run_GrasshopperReloadAssemblies() -> List: ...
    def Run_GrasshopperExportHelp() -> bool: ...
    def Run_GrasshopperGetSDKDocumentation() -> bool: ...
    def Run_GrasshopperBake() -> bool: ...
    def Run_GrasshopperFolders() -> bool: ...
    @property
    def BakeDocument() -> GH_Document: ...
    @BakeDocument.setter
    def BakeDocument(Value: GH_Document) -> None: ...
    @property
    def BakeObject() -> IGH_ActiveObject: ...
    @BakeObject.setter
    def BakeObject(Value: IGH_ActiveObject) -> None: ...


class GH_RhinoScriptInterface:
    def __init__(self): ...
    def IsEditorLoaded(self) -> bool: ...
    def IsEditorVisible(self) -> bool: ...
    def LoadEditor(self) -> None: ...
    def ShowEditor(self) -> None: ...
    def HideEditor(self) -> None: ...
    def EnableBanner(self) -> None: ...
    def DisableBanner(self) -> None: ...
    def IsSolverEnabled(self) -> bool: ...
    def EnableSolver(self) -> None: ...
    def DisableSolver(self) -> None: ...
    def RunSolver(self, expireAllObjects: bool) -> None: ...
    def OpenDocument(self, filename: str) -> bool: ...
    def CloseDocument(self) -> bool: ...
    def CloseAllDocuments(self) -> bool: ...
    def SaveDocument(self) -> bool: ...
    def SaveDocumentAs(self, filename: str) -> bool: ...
    def AssignDataToParameter(self, parameterID: str, data: Object) -> bool: ...
    def SetSliderValue(self, sliderID: str, value: float) -> bool: ...
    def SetSliderRangeAndValue(self, sliderID: str, value: float, minimum: float, maximum: float) -> bool: ...
    def BakeDataInObject(self, objectID: str) -> Object: ...
    def RunHeadless(self) -> None: ...