from requests import Session
import logging
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from utils.constants import CONNECT_TIMEOUT, READ_TIMEOUT
from requests.exceptions import (
    Timeout,
    HTTPError,
    RequestException,
    ReadTimeout,
    ConnectTimeout,
)
from requests import ConnectionError


class ServiceApi:
    def __init__(self, session: Session, url: str, token: str) -> None:
        self._session = session
        self._base_url = url
        self._token = token
        self._http_adapter = HTTPAdapter(max_retries=3)
        self._session.mount(self._base_url, self._http_adapter)
        self._session.headers.update(self.get_headers())
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Token {self._token}",
        }

    def post(self, url: str, data: dict) -> None:
        err_res = {}
        with self._session as session:
            try:
                res = session.post(
                    url=url,
                    json=data,
                    verify=False,
                    timeout=(CONNECT_TIMEOUT, READ_TIMEOUT),
                )
                res.raise_for_status()
            except ConnectionError as ce:
                error_msg = f"ConnectionError: {str(ce)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except Timeout as to:
                error_msg = f"Timeout: {str(to)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except ReadTimeout as rt:
                error_msg = f"ReadTimeout: {str(rt)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except ConnectTimeout as ct:
                error_msg = f"ConnectTimeout: {str(ct)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except HTTPError as he:
                error_msg = f"HTTPError: {str(he)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except RequestException as re:
                error_msg = f"RequestException: {str(re)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            else:
                self.logger.info(f"Success With Request")
        return res.json()

    def get(self, url: str, data: dict) -> None:
        err_res = {}
        with self._session as session:
            try:
                res = session.get(
                    url=url,
                    json=data,
                    verify=False,
                    timeout=(CONNECT_TIMEOUT, READ_TIMEOUT),
                )
                res.raise_for_status()
            except ConnectionError as ce:
                error_msg = f"ConnectionError: {str(ce)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except Timeout as to:
                error_msg = f"Timeout: {str(to)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except ReadTimeout as rt:
                error_msg = f"ReadTimeout: {str(rt)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except ConnectTimeout as ct:
                error_msg = f"ConnectTimeout: {str(ct)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except HTTPError as he:
                error_msg = f"HTTPError: {str(he)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            except RequestException as re:
                error_msg = f"RequestException: {str(re)}"
                self.logger.exception(error_msg)
                err_res["b2c2_error"] = error_msg
                return err_res
            else:
                self.logger.info(f"Success With Request")
        return res.json()

    def post_data(self, relative_url: str, data: dict) -> None:
        self.logger.info(f"Relative URL: {relative_url}")
        url = urljoin(
            self._base_url,
            relative_url,
        )
        self.logger.info(f"Requested Data: {data}")
        self.logger.info(f"New URL: {url}")
        return self.post(url, data)

    def get_data(self, relative_url: str, data: dict) -> None:
        url = urljoin(self._base_url, relative_url)
        self.logger.info(f"New URL: {url}")
        self.logger.info(f"Requested Data: {data}")
        return self.get(url, data)

    # def validate_error(self, response: dict) -> None:
    #     if "error" in response:
    #         return f"Error Detected: {response}"
    #     else:
    #         return response