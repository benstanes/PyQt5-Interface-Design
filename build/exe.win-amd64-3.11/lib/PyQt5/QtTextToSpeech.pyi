# The PEP 484 type hints stub file for the QtTextToSpeech module.
#
# Generated by SIP 6.7.6
#
# Copyright (c) 2023 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

import PyQt5.sip

from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QTextToSpeech(QtCore.QObject):

    class State(int):
        Ready = ... # type: QTextToSpeech.State
        Speaking = ... # type: QTextToSpeech.State
        Paused = ... # type: QTextToSpeech.State
        BackendError = ... # type: QTextToSpeech.State

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, engine: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    voiceChanged: typing.ClassVar[QtCore.pyqtsignal]
    volumeChanged: typing.ClassVar[QtCore.pyqtsignal]
    pitchChanged: typing.ClassVar[QtCore.pyqtsignal]
    rateChanged: typing.ClassVar[QtCore.pyqtsignal]
    localeChanged: typing.ClassVar[QtCore.pyqtsignal]
    stateChanged: typing.ClassVar[QtCore.pyqtsignal]
    def setVoice(self, voice: 'QVoice') -> None: ...
    def setVolume(self, volume: float) -> None: ...
    def setPitch(self, pitch: float) -> None: ...
    def setRate(self, rate: float) -> None: ...
    def setLocale(self, locale: QtCore.QLocale) -> None: ...
    def resume(self) -> None: ...
    def pause(self) -> None: ...
    def stop(self) -> None: ...
    def say(self, text: str) -> None: ...
    @staticmethod
    def availableEngines() -> typing.List[str]: ...
    def volume(self) -> float: ...
    def pitch(self) -> float: ...
    def rate(self) -> float: ...
    def availableVoices(self) -> typing.List['QVoice']: ...
    def voice(self) -> 'QVoice': ...
    def locale(self) -> QtCore.QLocale: ...
    def availableLocales(self) -> typing.List[QtCore.QLocale]: ...
    def state(self) -> 'QTextToSpeech.State': ...


class QVoice(PyQt5.sipsimplewrapper):

    class Age(int):
        Child = ... # type: QVoice.Age
        Teenager = ... # type: QVoice.Age
        Adult = ... # type: QVoice.Age
        Senior = ... # type: QVoice.Age
        Other = ... # type: QVoice.Age

    class Gender(int):
        Male = ... # type: QVoice.Gender
        Female = ... # type: QVoice.Gender
        Unknown = ... # type: QVoice.Gender

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QVoice') -> None: ...

    @staticmethod
    def ageName(age: 'QVoice.Age') -> str: ...
    @staticmethod
    def genderName(gender: 'QVoice.Gender') -> str: ...
    def age(self) -> 'QVoice.Age': ...
    def gender(self) -> 'QVoice.Gender': ...
    def name(self) -> str: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...
